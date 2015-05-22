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

from ovirtsdk.xml import params
import types

class OvirtSdkError(Exception):
    def __init__(self, content):
        Exception.__init__(self, content)

class ConnectionError(Exception):
    def __init__(self, expect):
        Exception.__init__(self, '[ERROR]::oVirt API connection failure, %s' % expect)

class NoCertificatesError(Exception):
    def __init__(self):
        Exception.__init__(self, '[ERROR]::ca_file (CA certificate) must be specified for SSL connection.')

class DisconnectedError(Exception):
    def __init__(self):
        Exception.__init__(self, '[ERROR]::oVirt sdk is disconnected from the server.')

class UnsecuredConnectionAttemptError(Exception):
    def __init__(self):
        Exception.__init__(self, "[ERROR]::No response returned from server. If you're using HTTP protocol\n" + \
                                 "against a SSL secured server, then try using HTTPS instead.")

class MissingParametersError(Exception):
    def __init__(self, params):
        Exception.__init__(self, "[ERROR]::One of the following parameters has to be specified: %s." % params)

class RequestError(Exception):
    def __init__(self, response_code, response_reason, response_body):
        self.detail = None
        self.status = None
        self.reason = None
        detail = ''
        RESPONSE_FORMAT = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        RESPONSE_FAULT_BODY = '<fault>'
        APP_SERVER_RESPONSE_FORMAT = '<html><head><title>JBoss Web'

        # REST error
        if response_body and response_body.startswith(RESPONSE_FORMAT) and response_body.find(RESPONSE_FAULT_BODY) != -1:
            try:
                f_detail = params.parseString(response_body, silence=True)
            except:
                f_detail = ''

            if str != type(f_detail):
                if isinstance(f_detail, params.Action) and f_detail.fault is not None:
                    detail = f_detail.fault.detail.lstrip()
                else:
                    if f_detail and f_detail.detail:
                        detail = f_detail.detail.lstrip()

                # engine returns can-do-action error messages with brackets
                if detail and detail.startswith('[') and detail.endswith(']'):
                    detail = detail[1:len(detail) - 1]

        # application server error
        elif response_body.startswith(APP_SERVER_RESPONSE_FORMAT):
            detail = response_body
            start = detail.find('<h1>')
            end = detail.find('</h1>')
            if start != -1 and end != -1:
                detail = detail[start:end].replace('<h1>', '').replace('</h1>', '')
                if detail and detail.endswith(' - '):
                    detail = detail[:len(detail) - 3]
        else:
            detail = '\n' + response_body if response_body else ''

        self.detail = detail
        self.reason = response_reason
        self.status = response_code

        Exception.__init__(self, '[ERROR]::oVirt API request failure.' + self.__str__())

    def __str__(self):
        return '\r\nstatus: ' + str(self.status) + '\r\nreason: ' + self.reason + '\r\ndetail: ' + str(self.detail)

class ImmutableError(Exception):
    def __init__(self, key):
        Exception.__init__(self, '[ERROR]::\'%s\' is immutable.' % key)

class FormatError(Exception):
    def __init__(self):
        Exception.__init__(self, '[ERROR]::Server reply is in inappropriate format.')

class AmbiguousQueryError(OvirtSdkError):
    def __init__(self, query=None):
        Exception.__init__(
           self,
           '[ERROR]::Used query %s produces ambiguous results.'
                % ("(" + query + ")" if query and query != "" else "")
        )
