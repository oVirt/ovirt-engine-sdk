'''
Created on Oct 24, 2011

@author: mpastern
'''

class UrlHelper(object):
    @staticmethod
    def replace(url, args={}):
        for k,v in args.items():
            url = url.replace(k, v)
        return url