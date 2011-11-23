'''
Created on Oct 16, 2011

@author: mpastern
'''
from Queue import Queue
import thread
from ovirtsdk.web.connection import Connection

class ConnectionsPool(object):
    '''
    ConnectionsManager used to manage pool of web connections
    '''
    def __init__(self, url, port, key_file, cert_file, strict, timeout, username, password, count=20):

        self.__free_connetcions = Queue(0)
        self.__busy_connetcions = {}

        self.__plock = thread.allocate_lock()
        self.__rlock = thread.allocate_lock()

        self.__url = url

        for _ in range(count):
            self.__free_connetcions.put(item=Connection(url=url, \
                                                        port=port, \
                                                        key_file=key_file, \
                                                        cert_file=cert_file, \
                                                        strict=strict, \
                                                        timeout=timeout, \
                                                        username=username, \
                                                        password=password,
                                                        manager=self))
    def getConnection(self, get_ttl=100):
#        try:
            with self.__plock:
                conn = self.__free_connetcions.get(block=True, timeout=get_ttl)
                self.__busy_connetcions[conn.get_id()] = conn
                return conn
#        except Empty, e:
#                self.__extendQueue()
#                return self.getConnection(get_ttl)

#    def __extendQueue(self):
#TODO: add more connections if needed
#        continue

    def _freeResource(self, conn):
        with self.__rlock:
            conn = self.__busy_connetcions.pop(conn.get_id())
            self.__free_connetcions.put_nowait(conn)

    def get_url(self):
        return self.__url
