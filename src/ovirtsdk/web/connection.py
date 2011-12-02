'''
Created on Oct 9, 2011

@author: mpastern
'''

import base64
from httplib import HTTPConnection, HTTPSConnection
import urllib
import urlparse

class Connection(object):
    '''
    The oVirt api connection proxy
    '''
    def __init__(self, url, port, key_file, cert_file, strict, timeout, username, password, manager):
        self.__connetcion = self.__createConnection(url=url,
                                                    port=port,
                                                    key_file=key_file,
                                                    cert_file=cert_file,
                                                    strict=strict,
                                                    timeout=timeout)
        self.__headers = self.__createHeaders(username, password)
        self.__manager = manager
        self.__id = id(self)

    def get_id(self):
        return self.__id

    def getConnection(self):
        return self.__connection

    def getDefaultHeaders(self):
        return self.__headers

    def doRequest(self, method, url, body=urllib.urlencode({}), headers={}):
        return self.__connetcion.request(method, url, body, self.getHeaders(headers))

    def getHeaders(self, headers):
        extended_headers = self.getDefaultHeaders()
        for k in headers.keys():
            if (headers[k] is None and extended_headers.has_key(k)):
                extended_headers.pop(k)
            else:
                extended_headers[k] = headers[k]
        return extended_headers

    def getResponse(self, buffering=False):
        return self.__connetcion.getresponse(buffering)

    def setDebugLevel(self, level):
        self.__connection.set_debuglevel(level)

    def setTunnel(self, host, port=None, headers=None):
        self.__connection.set_tunnel(host, port, headers)

    def close(self):
        self.__connetcion.close()
#FIXME: create connection watchdog to close it on idle-ttl expiration, rather than after the call
        if (self.__manager is not None):
            self.__manager._freeResource(self)

    def __createConnection(self, url, key_file=None, cert_file=None, port=None, strict=None, timeout=None, source_address=None):
        u = urlparse.urlparse(url)
        if(u.scheme == 'https'):
            return HTTPSConnection(host=u.hostname,
                                   port=u.port,
                                   key_file=key_file,
                                   cert_file=cert_file,
                                   strict=strict,
                                   timeout=timeout,
                                   source_address=source_address)
        return HTTPConnection(host=u.hostname,
                              port=u.port,
                              strict=strict,
                              timeout=timeout)

    def __createHeaders(self, username, password):
        auth = base64.encodestring("%s:%s" % (username, password)).strip()
        return {"Content-type": "application/xml", "Authorization": "Basic %s" % auth}
    id = property(get_id, None, None, None)

#    connection = property(get_connection, None, None, None)
#    headers = property(get_headers, None, None, None)


