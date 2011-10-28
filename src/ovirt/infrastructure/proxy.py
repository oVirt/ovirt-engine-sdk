'''
Created on Oct 17, 2011

@author: mpastern
'''

import socket
from ovirt.infrastructure.errors import RequestError, ConnectionError
from ovirt.xml import params

class Proxy():
    '''
    The proxy to web connection
    '''
    def __init__(self, connections_pool):
        """Constructor."""
        self.__connections_pool = connections_pool

    def getConnectionsPool(self):
        return self.__connections_pool

    def get(self, url, headers={}):
        return self.request(method='GET', url=url, headers=headers)
    
    def delete(self, url, body=None, headers={}):
        return self.request('DELETE', url, body, headers)

    def update(self, url, body=None, headers={}):
        return self.request('PUT', url, body, headers)
    
    def add(self, url, body=None, headers={}):
        return self.request('POST', url, body, headers)
    
    def action(self, url, body=None, headers={}):
        return self.request('POST', url, body, headers)
    
    def request(self, method, url, body=None, headers={}):
        return self.__doRequest(method,\
                                url,\
                                body=body,\
                                headers=headers,\
                                conn=self.getConnectionsPool().getConnection())
            
    def __doRequest(self, method, url, conn, body=None, headers={}):
        try:
            conn.doRequest(method=method, url=url, body=body, headers=headers)
            response = conn.getResponse()
            if (response.status < 400):
                res = response.read()
                return params.parseString(res) if res is not None and res is not '' else res
            else:
                raise RequestError, response
        except socket.error, e:
            raise ConnectionError, str(e)
        finally:
            conn.close()
    
    @staticmethod
    def instance(connections_pool):
        Proxy(connections_pool)