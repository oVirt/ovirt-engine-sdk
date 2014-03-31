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

import httplib
import re
import socket
import ssl


class HTTPSConnection(httplib.HTTPSConnection):
    '''
    This class is httplib.HTTPSConnection decorator providing
    server certificate validation capabilities.
    '''

    def __init__(self, host, port=None, key_file=None, cert_file=None, ca_file=None,
                 strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                 insecure=False):
        httplib.HTTPSConnection.__init__(self, host=host, port=port, key_file=key_file,
                                         cert_file=cert_file, strict=strict, timeout=timeout)
        self.ca_file = ca_file
        self.insecure = insecure

    def connect(self):
        '''
        httplib.HTTPSConnection.connect() clone that connects to a host on a given (SSL) port, 
        but forcing ssl.CERT_REQUIRED if ca_file has been specified.
        '''

        sock = socket.create_connection((self.host, self.port),
                                        self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()

        if self.ca_file:
            self.sock = ssl.wrap_socket(
                sock,
                self.key_file,
                self.cert_file,
                ca_certs=self.ca_file,
                cert_reqs=ssl.CERT_REQUIRED
            )
        else:
            self.sock = ssl.wrap_socket(
                sock,
                self.key_file,
                self.cert_file,
                cert_reqs=ssl.CERT_NONE
            )

        # Check that the host name contained in the URL matches at least one of
        # the host names contained in the server certificate:
        if not self.insecure:
            cert = self.sock.getpeercert()
            if not self.__check_host_name(cert):
                raise httplib.HTTPException(
                    "The host name \"%s\" contained in the URL doesn't match "
                    "any of the names in the server certificate." % self.host)

    def __check_host_name(self, cert):
        """
        Checks that the host name given in the URL matches the name
        included in the certificate.
        """
        # Extract all the names and IP addresses from the certificate:
        cn = self.__get_last_cn(cert)
        alt_names = self.__get_alt_names(cert, "DNS")
        alt_ips = self.__get_alt_names(cert, "IP Address")

        # If host name contained in the URL is actually an IP address then we
        # need to compare it to the alternative IP addresses included in the
        # server certificate:
        host_ip = self.__parse_ip(self.host)
        if host_ip and alt_ips:
            for alt_ip in alt_ips:
                alt_ip = self.__parse_ip(alt_ip)
                if host_ip == alt_ip:
                    return True
            return False

        # If there are DNS alternative names then we should compare the host
        # name in the URL to these names:
        if alt_names:
            for alt_name in alt_names:
                if self.__check_name(self.host, alt_name):
                    return True
            return False

        # If there are no alternative DNS names then we should compare the host
        # name to the common name of the subject of the certificate:
        cn = self.__get_last_cn(cert)
        if cn:
            return self.__check_name(self.host, cn)

        # There is no match:
        return False

    def __get_alt_names(self, cert, category):
        """
        Returns a list containing alternative names of a given category
        contained in a certificate.
        """
        result = []
        extension = cert.get("subjectAltName")
        if extension:
            for key, value in extension:
                if key == category:
                    result.append(value)
        return result

    def __get_last_cn(self, cert):
        """
        Returns the last CN from the subject of a certificate, or None if the
        subject doesn't contain any CN.
        """
        result = None
        subject = cert.get("subject")
        if subject:
            for rdn in subject:
                for key, value in rdn:
                    if key == "commonName":
                        result = value
        return result

    def __check_name(self, name, pattern):
        """
        Checks if a host name matches a pattern. The only special character in
        this pattern is the asterisk, which matches any number of characters,
        except the dot. Returs True if the name matches, and False otherwise.
        """
        pattern = re.escape(pattern)
        pattern = pattern.replace("\\*", "[^.]*")
        pattern = "^" + pattern + "$"
        return re.match(pattern, name, re.IGNORECASE)

    def __parse_ip(self, addr):
        """
        Parses an IPv4 or IPv6 address and converts it to its binary
        representation. Returns None if the given address string isn't a
        valid IP address.
        """
        try:
            return socket.inet_pton(socket.AF_INET, addr)
        except socket.error:
            pass
        try:
            return socket.inet_pton(socket.AF_INET6, addr)
        except socket.error:
            pass
        return None
