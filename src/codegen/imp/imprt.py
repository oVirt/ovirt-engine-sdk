'''
Created on Oct 24, 2011

@author: mpastern
'''
import datetime

#============================================================
#==========================IMPORTS===========================
#============================================================

intro = "\n\n########################################\n" + \
        "############ GENERATED CODE ############\n" + \
        "########################################\n\n"

stamp = \
"'''\nGenerated at: " + str(datetime.datetime.now()) + "\n\n" + \
"@author: mpastern@redhat.com\n'''\n\n"

imports = intro + stamp + \
"from ovirtsdk.xml import params\n" + \
"from ovirtsdk.utils.urlhelper import UrlHelper\n" + \
"from ovirtsdk.utils.filterhelper import FilterHelper\n" + \
"from ovirtsdk.utils.parsehelper import ParseHelper\n" + \
"from ovirtsdk.utils.searchhelper import SearchHelper\n" + \
"from ovirtsdk.infrastructure.common import Base\n\n\n"

class Import(object):
    @staticmethod
    def getimports(): return imports
