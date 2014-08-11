# Copyright (c) 2010 IBM.
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
# this configure is used to generate the params.py
# but this configure should comply with python grammar
# this maybe useful, for some editor such as vi or Eclipse
# can show the python prammar to avoid some error

# now I have not find a good way to delete several lines of code
# in the params.py. for there will be same in other place of th file.
# so the regular expresion can not work well. even if exact match.
# if you want to modify several lines of code in a function,
# your should prepare a new function code to take the whole funciton.

# configure the import moudule
modules = ["from ovirtsdk.utils.reflectionhelper import ReflectionHelper",
           "from ovirtsdk.utils.comperator import Comparator"]


# attributes of certain class, will be append to this calls in params.py
_generatedsSuperAttribute = """
# Begin NOT_GENERATED
def __setattr__(self, item, value):
    if (value is not None and
        not isinstance(value, list) and
        ReflectionHelper.isModuleMember(
            sys.modules['ovirtsdk.infrastructure.brokers'],
            type(value)) and
        not ReflectionHelper.isModuleMember(sys.modules[__name__],
            type(value)) and
        value.__dict__.has_key('superclass') and
        value.superclass is not None and
        value.superclass != BaseResource):
        if (ReflectionHelper.isModuleMember(
                sys.modules['ovirtsdk.infrastructure.brokers'],
                type(self)) and
           self.__dict__.has_key('superclass') and
           self.superclass is not None):
            object.__setattr__(self.superclass, item, value.superclass)
        else:
            object.__setattr__(self, item, value.superclass)
    elif (not isinstance(value, list) and
         ReflectionHelper.isModuleMember(
                 sys.modules['ovirtsdk.infrastructure.brokers'],
                 type(self)) and
         self.__dict__.has_key('superclass') and
         self.superclass is not None and
         not ReflectionHelper.isModuleMember(
                 sys.modules['ovirtsdk.infrastructure.brokers'],
                 type(value)) and
         item is not 'superclass' and
         item is not 'parentclass'):
        object.__setattr__(self.superclass, item, value)
    elif isinstance(value, list):
        parsed_list = []
        for obj in value:
            if (ReflectionHelper.isModuleMember(
                    sys.modules['ovirtsdk.infrastructure.brokers'],
                    type(obj)) and
               obj.__dict__.has_key('superclass') and
               obj.superclass is not None and
               item is not 'superclass' and
               item is not 'parentclass'):
                parsed_list.append(obj.superclass)
            else:
                parsed_list.append(obj)
        object.__setattr__(self, item, parsed_list)
    else:
        object.__setattr__(self, item, value)

def __eq__(self, other):
    return Comparator.compare(self, other)

def __ne__(self, other):
    return not self.__eq__(other)
# End NOT_GENERATED
"""

#the function dict which will be added to the params.py
#key: the class name,
#value: the attribut of class
addfunctionlist = {
        "GeneratedsSuper": _generatedsSuperAttribute}

_findRootClass = """
def findRootClass(rootTag):
    \"\"\"
    Helper function that enables the generated code to locate the
    root element.  The api does not explicitly list a root
    element; hence, the generated code has a hard time deducing
    which one it actually is.  This function will map the first
    tag in the XML (i.e. the root) to an internal class.
    \"\"\"
    return _rootClassMap.get(rootTag)
"""

# function list which will be added to the params.py
globalfunctionlist = [_findRootClass]

_getRootTag = r"""
def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    #rootClass = globals().get(tag)
    # Begin NOT_GENERATED
    # The api XSD does not define a single root tag.
    # We need to map the classes in this file to the possible
    # element roots in the XSD.
    # rootClass = globals().get(tag)
    rootClass = findRootClass(tag)
    # End NOT_GENERATED
    return tag, rootClass
"""
#there is a '\n' in this docstring, so should use raw string
_parseString = r"""
def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'link'
        rootClass = Link
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # Begin NOT_GENERATED
    # Let's shut up the echoing of the received XML
    # to stdout.
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="link",
    #    namespacedef_='')
    # End NOT_GENERATED
    return rootObj
"""

# functions in the following dict will replace the functions with the same
# names in params.py
# key: the function name,
# value:
#       first, the function body string.
#       second, which class the functon belong to, empty class name means
#               the target function is a global function

substitutefunctionlist = {"get_root_tag": [_getRootTag, ""],
                          "parseString": [_parseString, ""]}


#this class list are in __all__ list, but excluded in _rootClassMap
excludeInRootClassMap = [
    "BaseDevice",
    "BaseDevices",
    "BaseResource",
    "BaseResources",
    "ErrorHandlingOptions",
    "DetailedLink"
    ]
