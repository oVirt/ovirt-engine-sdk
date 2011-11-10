'''
Created on Oct 24, 2011

@author: mpastern
'''
import datetime

#============================================================
#==========================IMPORTS===========================
#============================================================

intro = "\n\n########################################\n"+\
        "############ GENERATED CODE ############\n"+\
        "########################################\n\n"

stamp =\
"'''\nGenerated at: "+ str(datetime.datetime.now())+"\n\n"+\
"@author: mpastern@redhat.com\n'''\n\n"

imports = intro + stamp +\
"from ovirt.xml import params\n"+\
"from ovirt.utils.urlhelper import UrlHelper\n"+\
"from ovirt.utils.filterhelper import FilterHelper\n"+\
"from ovirt.utils.parsehelper import ParseHelper\n"+\
"from ovirt.utils.searchhelper import SearchHelper\n"+\
"from ovirt.infrastructure.common import Base\n\n\n"

class Import(object):
    @staticmethod
    def getimports(): return imports