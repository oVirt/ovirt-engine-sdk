#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import cStringIO
import pycurl
import threading

from ovirtsdk.infrastructure import errors
from ovirtsdk.infrastructure.context import context


class ConnectionsPool(object):
    """Object used to manage pool of HTTP connections"""

    def __init__(self, url, key_file, cert_file, ca_file, timeout, username,
                 password, context_key, insecure, validate_cert_chain, debug,
                 kerberos):
        # Save the URL and the context key:
        self.__url = url
        self.__context_key = context_key

        # Save the credentials:
        self.__username = username
        self.__password = password
        self.__kerberos = kerberos

        # The curl object can be used by several threads, but not
        # simultaneously, so we need a lock to prevent that:
        self.__curl_lock = threading.Lock()

        # Create the curl handle that manages the pool of connections:
        self.__curl = pycurl.Curl()
        self.__curl.setopt(pycurl.COOKIEFILE, "/dev/null")
        self.__curl.setopt(pycurl.COOKIEJAR, "/dev/null")

        # Configure SSH parameters:
        if url.startswith("https"):
            if validate_cert_chain:
                if not insecure and not ca_file:
                    raise errors.NoCertificatesError
            else:
                ca_file = None
            self.__curl.setopt(pycurl.SSL_VERIFYPEER, 0 if insecure else 1)
            self.__curl.setopt(pycurl.SSL_VERIFYHOST, 0 if insecure else 2)
            if ca_file is not None:
                self.__curl.setopt(pycurl.CAINFO, ca_file)
            if cert_file is not None and key_file is not None:
                self.__curl.setopt(pycurl.SSLCERTTYPE, "PEM")
                self.__curl.setopt(pycurl.SSLCERT, cert_file)
                self.__curl.setopt(pycurl.SSLKEY, key_file)

        # Configure timeouts:
        if timeout is not None:
            self.__curl.setopt(pycurl.TIMEOUT, timeout)

        # Configure debug mode:
        if debug:
            self.__curl.setopt(pycurl.VERBOSE, 1)
            self.__curl.setopt(pycurl.DEBUGFUNCTION, self.__curl_debug)

    def do_request(self, method, url, body=None, headers={}, last=False,
                   persistent_auth=True):
        with self.__curl_lock:
            try:
                return self.__do_request(method, url, body, headers, last,
                                         persistent_auth)
            except pycurl.error as error:
                raise errors.ConnectionError(error)

    def __do_request(self, method, url, body, headers, last,
                    persistent_auth):
        # Set the method:
        self.__curl.setopt(pycurl.CUSTOMREQUEST, method)

        # Set the URL:
        self.__curl.setopt(pycurl.URL, self.__url + url)

        # Basic credentials should be sent only if there isn't a session:
        if self.__kerberos:
            self.__curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_GSSNEGOTIATE)
            self.__curl.setopt(pycurl.USERPWD, ":")
        elif not self.__in_session():
            self.__curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
            self.__curl.setopt(pycurl.USERPWD, "%s:%s" % (self.__username, self.__password))

        # Add headers, avoiding those that have no value:
        header_lines = []
        for header_name, header_value in headers.items():
            if header_value is not None:
                header_lines.append("%s: %s" % (header_name, header_value))
        header_lines.append("Version: 3")
        header_lines.append("Content-Type: application/xml")
        header_lines.append("Accept: application/xml")

        # Set the filter header:
        fltr = context.manager[self.__context_key].get("filter")
        if fltr is not None:
            header_lines.append("Filter: %s" % fltr)

        # Set the session TTL header:
        ttl = context.manager[self.__context_key].get("session_timeout")
        if ttl is not None:
            header_lines.append("Session-TTL: %s" % ttl)

        # Every request except the last one should indicate that we prefer
        # to use persistent authentication:
        if persistent_auth and not last:
            header_lines.append("Prefer: persistent-auth")

        # Copy headers and the request body to the curl object:
        self.__curl.setopt(pycurl.HTTPHEADER, header_lines)
        self.__curl.setopt(pycurl.POSTFIELDS, body if body is not None else "")

        # Prepare the buffers to receive the response:
        body_buffer = cStringIO.StringIO()
        headers_buffer = cStringIO.StringIO()
        self.__curl.setopt(pycurl.WRITEFUNCTION, body_buffer.write)
        self.__curl.setopt(pycurl.HEADERFUNCTION, headers_buffer.write)

        # Send the request and wait for the response:
        self.__curl.perform()

        # Extract the response code and body:
        response_code = self.__curl.getinfo(pycurl.HTTP_CODE)
        response_body = body_buffer.getvalue()

        # The response code can be extracted directly, but culr doesn't
        # have a method to extract the response message, so we have to
        # parse the first header line to find it:
        response_reason = ""
        header_lines = headers_buffer.getvalue().split("\n")
        if len(header_lines) >= 1:
            response_line = header_lines[0]
            response_fields = response_line.split()
            if len(response_fields) >= 3:
                response_reason = " ".join(response_fields[2:])

        # Parse the received body only if there are no errors reported by
        # the server (this needs review, as less than 400 doesn't guarantee
        # a correct response, it could be a redirect, and many other
        # things):
        if response_code >= 400:
            raise errors.RequestError(response_code, response_reason, response_body)

        return response_body

    def close(self):
        with self.__curl_lock:
            self.__curl.close()

    @staticmethod
    def __curl_debug(debug_type, debug_message):
        prefix = "* "
        if debug_type == pycurl.INFOTYPE_DATA_IN:
            prefix = "< "
        elif debug_type == pycurl.INFOTYPE_DATA_OUT:
            prefix = "> "
        elif debug_type == pycurl.INFOTYPE_HEADER_IN:
            prefix = "< "
        elif debug_type == pycurl.INFOTYPE_HEADER_OUT:
            prefix = "> "
        lines = debug_message.replace("\r\n", "\n").strip().split("\n")
        for line in lines:
            print("%s%s" % (prefix, line))

    def __in_session(self):
        for cookie_line in self.__curl.getinfo(pycurl.INFO_COOKIELIST):
            cookie_fields = cookie_line.split("\t")
            cookie_name = cookie_fields[5]
            if cookie_name == "JSESSIONID":
                return True
        return False

    def get_url(self):
        return self.__url
