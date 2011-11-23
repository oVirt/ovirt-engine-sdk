'''
Created on Oct 24, 2011

@author: mpastern
'''
from ovirtsdk.utils.searchhelper import SearchHelper

class FilterHelper():
    @staticmethod
    def filter(collection, kwargs={}):
        '''Filters collection based on **kwargs'''
        return SearchHelper.filterResults(collection, kwargs) if (len(kwargs) is not 0) else collection

    @staticmethod
    def getItem(result=[]):
        '''Returns first item in collection if exist, otherwise None'''
        return result[0] if(result is not None and len(result) > 0) else None
