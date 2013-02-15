#!/usr/bin/python
#
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

import re
import sys
import subprocess
import os
import paramsconf
import argparse
import logging
import xml.dom.minidom

# sys.path.append("../../src/ovirtsdk/infrastructure/")
# import contextmanager

__version__ = '0.1.0'
PROG = 'genparams'

BEGINEGENERATE = "# Begin NOT_GENERATED"
ENDGENERATE = "# End NOT_GENERATED"
INDENTNUMS = 4
DEFRERULE = r'^\s*%s\s+%s(?:\([_\w\*,=]*\)):.*$'
CLASSRERULE = r'^\s*%s\s+%s(?:\([_\w]*\))?:.*$'
RESTFILE = "api.xsd"
OUTFILE = r"params.py"
LOGFILE = r"genparams.log"

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}


class helpAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        namespace._help = True
        parser.print_help()


class CmdLineParser(object):
    def __init__(self):
        prog = PROG
        description = """DESCRIPTION\
        \n    generate %s from FILE (the api.xsd in current directory \
        \n    by default) automatically.""" % OUTFILE
        usage = """\
        \n%(prog)s [OPTION]... [FILE]"""
        epilog = """COPYRIGHT\
        \n     Copyright (c) 2012 IBM\
        \n     Licensed under the Apache License, Version 2.0 (the "License");\
        \n     you may not use this file except in compliance with the License\
        \n     You may obtain a copy of the License at\
        \n          http://www.apache.org/licenses/LICENSE-2.0"""
        self.parser = argparse.ArgumentParser(
                prog=prog, usage=usage,
                epilog=epilog,
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=description,
                add_help=False)
        self.initParser()

    def initParser(self):
        self.parser.add_argument('-h', '--help', action=helpAction,
                                 nargs=0, default=argparse.SUPPRESS,
                                 help='show this help message')
        self.parser.add_argument('-o', metavar='FILE',
                                 default=OUTFILE, dest="outfile",
                                 help='the generatation output file, '
                                    'default ./%s' % OUTFILE)
        self.parser.add_argument('--server',
                                 help='rest api sever, '
                                    'default http://localhost:8080/')
        self.parser.add_argument('--logfile', default=LOGFILE,
                                 help='set the log file, '
                                   'default ./%s ' % LOGFILE)
        self.parser.add_argument('--version', action='version',
                                 version='%(prog)s ' + __version__)
        self.parser.add_argument('schemafile', nargs='?', default=RESTFILE,
                                 metavar='api schema file',
                                 help=argparse.SUPPRESS)
        self.parser.add_argument('remain',
                                 metavar='the remain arguments',
                                 nargs=argparse.REMAINDER,
                                 help=argparse.SUPPRESS)
        self.parser.set_defaults(func=self.run)

    def getHost(self):
        return self.host

    def getLogFile(self):
        return self.logFile

    def getSchemaFile(self):
        return self.schemaFile

    def getOutFile(self):
        return self.outFile

    def handle_command(self, argv):
        argsresult = self.parser.parse_args(argv)
        argsresult.func(argsresult)
        return argsresult

    def run(self, args):
        self.schemaFile = args.schemafile
        self.outFile = args.outfile
        self.logFile = args.logfile
        pass


def logConfigure(logFile, setLevel="debug"):
    FORMAT = '%(asctime)-15s line:%(lineno)d  %(message)s'
    logging.basicConfig(format=FORMAT, filename=logFile,
                        level=LEVELS[setLevel])


def _call(args):
    cmd = " ".join(args)
    try:
        rc = subprocess.call(cmd, shell=True)
    except OSError, e:
        print >> sys.stderr, "Execution failed:", e
    return rc


class symbolInterpret(object):
    def __init__(self):
        pass

    @classmethod
    def classReRule(cls):
        rule1 = r'^\s*class\s+[_\w]+\s*:.*$'
        rule2 = r'^\s*class\s+[_\w]+\([_\w\s,]*\)\s*:.*$'
        rule = '|'.join([rule1, rule2])
        return rule

    @classmethod
    def classAndAttrReRule(cls):
        attrrule = r'^\s+def\s+[_\w]+\s*\([_\w\s\*,]*\)\s*:.*$'
        rule = '|'.join([cls.classReRule(), attrrule])
        return rule

    @classmethod
    def listAllClassAndAttribute(cls, string):
        rule = cls.classAndAttrReRule()
        p = re.compile(rule, re.M)
        match = p.findall(string)
        return  match

    @classmethod
    def listAllGloableFunction(cls, string):
        rule = r'^def\s+[_\w]+\s*\([_\w\s\*,]*\)\s*:.*$'
        p = re.compile(rule, re.M)
        match = p.findall(string)
        return  match

    @classmethod
    def getSymbolOfFile(cls, string):
        rule = r'\n\s*class\s+[_a-zA-Z0-9]*.*|\n\s*def\s+[_a-zA-Z0-9]*.*'
        p = re.compile(rule, re.M)
        match = p.findall(string)
        p = re.compile(r'^\n*')
        for i in range(len(match)):
            match[i] = p.sub('', match[i])
        return match

    @classmethod
    def getfunItemFromSymbolList(cls, symbol, symbols):
        rule = (r'^\s*def\s%s\((?:\*{0,2}[_\w]*)?\):\s*(?:#.*|$)',
                 "symbol")
        p = re.compile(rule, re.M)
        for val in symbols:
            if p.match(val):
                return re.sub(r'^\n*', '', val)
        return None

    @classmethod
    def getClassItemFromSymbolList(cls, symbol, symbols):
        rule = DEFRERULE % ("def", symbol)
        p = re.compile(rule, re.M)
        for val in symbols:
            if p.match(rule):
                return re.sub(r'^\n*', '', val)
        return None

    @classmethod
    def isClass(cls, symbolItem):
        rule = r'^\s*class\s[_a-zA-Z0-9]*.*'
        p = re.compile(rule, re.M)
        mat = p.match(symbolItem)
        if mat:
            return True
        return False

    @classmethod
    def isFunction(cls, symbolItem):
        rule = r'^\s*def\s+[_\w]+\s*\([_\w\s\*=,]*\)\s*:.*$'
        p = re.compile(rule, re.M)
        mat = p.match(symbolItem)
        if mat:
            return True
        return False

    @classmethod
    def getGlobalFun(cls, attri, symbols=[]):
        attrrule = r'^def\s+%s\s*\([_\w\s\*,]*\)\s*:.*$' % attri
        p = re.compile(attrrule, re.M)
        for val in symbols:
            m = p.match(val)
            if m:
                return val
        return None

    @classmethod
    def rsdlRootClass(cls, symbols):
        ruleGen = r'(?<=class\s).*(?=\(GeneratedsSuper\):)'
        ruleBase = r'(?<=class\s).*(?=\(BaseResource\):)'
        ruleLink = r'(?<=class\s).*(?=\(Link\):)'
        ruleBaseDevices = r'(?<=class\s).*(?=\(BaseDevices\):)'

        rule = '|'.join([ruleGen, ruleBase, ruleLink, ruleBaseDevices])
        classMap = []
        p = re.compile(rule, re.M)
        for val in symbols:
            mat = p.findall(val)
            if mat:
                classMap.append(mat[0])
        classMap.sort()
        return classMap


class symbolHandle(symbolInterpret):

    # there can be same sub-class name in two different classes
    # I just suppose it is unlikely
    # do not support the class nest
    @classmethod
    def classIndexInSymbols(cls, classname, symbols=[]):
        if not classname or not symbols:
            return -1
        rule = CLASSRERULE % ("class", classname)
        p = re.compile(rule, re.M)
        for idx, val in enumerate(symbols):
            m = p.match(val)
            if m:
                return idx
        return -1

    @classmethod
    def indentsOfClass(cls, classItem):
        return classItem.find("class")

    @classmethod
    def getIndentsOfString(cls, line):
        line = line.expandtabs(INDENTNUMS)
        linelist = list(line)
        for idx, val in enumerate(linelist):
            if val != " ":
                return idx

    @classmethod
    def indentsOfFunction(cls, functionitem):
        return functionitem.find("def")

    @classmethod
    def indentsOfSymbol(cls, item):
        if cls.isFunction(item):
            return cls.indentsOfFunction(item)
        if cls.isClass(item):
            return cls.indentsOfClass(item)
        return -1

    @classmethod
    def symbolIndexInfile(cls, symbol, fileLines=[]):
        symbol = symbol.replace("\n", "")
        for idx, val in enumerate(fileLines):
            if val.find(symbol) > -1:
                return idx
        return -1

    @classmethod
    def lastLineOfClass(cls, indents, start=0, fileLines=[]):
        match = []
        for i in range(start, len(fileLines)):
            match.append(fileLines[i])
            if (fileLines[i].strip() and
                cls.getIndentsOfString(fileLines[i]) <= indents):
                for midx in range(0, len(match)):
                    val = match.pop()
                    if (val.strip() and
                        cls.getIndentsOfString(val) > indents):
                        return (i - midx)
        return len(fileLines)

    @classmethod
    def getAttributeOfClass(cls, attri, classname, symbols=[]):
        idx = cls.classIndexInSymbols(classname, symbols)
        if idx == -1:
            return None, None
        attrrule = r'^\s+def\s+%s\s*\([_\w\s\*,]*\)\s*:.*$' % attri
        p = re.compile(attrrule, re.M)
        indents = cls.indentsOfClass(symbols[idx])
        for i in range(idx + 1, len(symbols), 1):
            if cls.isFunction(symbols[i]):
                if cls.indentsOfFunction(symbols[i]) > indents:
                    m = p.match(symbols[i])
                    if m:
                        return symbols[idx], symbols[i]
                else:
                    logging.error("[ERROR] wrong indent of item, "
                                  "%s in class %s",
                                  symbols[i], classname)
            elif cls.isClass(symbols[i]):
                return symbols[idx], None
            else:
                logging.error("[ERROR] a bad item:%s in symbols" % symbols[i])
        return symbols[idx], None

    @classmethod
    def findTheNextSymbol(cls, funline, idx, symbols):
        funindents = cls.indentsOfSymbol(funline)
        NextSymbol = None
        funcontext = []
        for i in range(idx + 1, len(symbols)):
            NextSymbol = symbols[i]
            if cls.indentsOfSymbol(NextSymbol) < funindents:
                funcontext.append(NextSymbol)
            else:
                return NextSymbol, i
        if not funcontext:
            return None, len(symbols)
        if cls.indentsOfSymbol(funcontext.pop()) < funindents:
            return None, len(symbols)


class paramsContext(symbolHandle):

    def __init__(self, files):
        self.files = files

    def getString(self, lines):
        return "\n".join(lines)

    def getLines(self, string):
        return string.split("\n")

    def operation(self):
        if _call(["which", "generateDS.py", ">/dev/null"]):
            logging.error('[ERROR] generateDS.py is not found, '
                          'please installed it')
            exit(1)
        if not os.path.exists(self.files["schema"]):
            logging.error('[ERROR] can not find the file %s',
                          (self.files["schema"]))
        if os.path.exists(self.files["target"]):
            os.unlink(self.files["target"])
        if os.path.exists(self.files["tmp"]):
            os.unlink(self.files["tmp"])
        _call(["generateDS.py", "-o", self.files["tmp"], self.files["schema"]])
        if not os.path.exists(self.files["tmp"]):
            logging.error('[ERROR] generate file %s by generateDS.py',
                          self.files["tmp"])
        with open(self.files["tmp"], "r") as fd:
            self.string = fd.read()
            fd.close()
        return self.string


class Decorator(paramsContext):

    def setComponet(self, paramsContext):
        self.paramsContext = paramsContext

    def operation(self):
        if (self.paramsContext):
            return self.paramsContext.operation()


class addModule(Decorator):

    def __init__(self, files):
        self.files = files

    def positon(self, string):
        # I suppose the code generated by generateDS should import some module.
        # and module import  at the head of file
        p = re.compile('\nimport.*\s(?!\nimport)')
        match = p.findall(string)
        self.pos = match.pop()

    def insert(self, modules, fileString):
        if not modules or not self.pos:
            return
        modules.insert(-2, self.pos)
        modules.insert(-2, BEGINEGENERATE)
        modules.append(ENDGENERATE + "\n")
        replace = "\n".join(modules)
        return re.sub(self.pos, replace, fileString, 1)

    def operation(self):
        string = Decorator.operation(self)
        logging.info("[INFO] add import module")
        self.positon(string)
        string = self.insert(paramsconf.modules, string)
        return string


class addClassAttri(Decorator):

    def __init__(self, files):
        self.files = files

    def positon(self, classname, symbols=[]):
        idx = self.classIndexInSymbols(classname, symbols)
        if idx == -1:
            self.pos = None
            return
        indents = self.indentsOfClass(symbols[idx])
        for i in range(idx + 1, len(symbols), 1):
            if self.getIndentsOfString(symbols[i]) <= indents:
                self.pos = symbols[i - 1]
                return
        self.pos = symbols[i]
        return

    def insert(self, start, indents, function, fileLines):
        preSpace = " " * indents
        if not function[len(function) - 1]:
            function.pop()
        if not function[0]:
            function.pop(0)
        for i in range(0, len(function)):
            if function[i]:
                line = preSpace + function[i]
            else:
                line = function[i]
            fileLines.insert(start + i + 1, line)
        return "\n".join(fileLines)

    def operation(self):
        string = Decorator.operation(self)
        symbols = self.getSymbolOfFile(string)
        for classname, attr in paramsconf.addfunctionlist.items():
            self.positon(classname, symbols)
            if not self.pos:
                logging.error("[ERROR] can not find the attribute of class %s",
                              classname)
                continue
            fileLines = self.getLines(string)
            attrLines = self.getLines(attr)
            indents = self.indentsOfSymbol(self.pos)
            if indents == -1:
                logging.error('[ERROR] can not calculate the indents of "%s"',
                              self.pos)
            idx = self.symbolIndexInfile(self.pos, fileLines)
            if idx == -1:
                logging.error("[ERROR] can not find the function in file: %s",
                              self.pos)
            line = self.lastLineOfClass(indents, idx, fileLines)
            string = self.insert(line, indents, attrLines, fileLines)
            logging.info("[INFO] add functions of class %s", classname)
        return string


class updataFunction(Decorator):

    def __init__(self, files):
        self.files = files

    def positon(self, classname, funline, nextsymbol, filelist):
        # state machine, fist find the class(step==0)
        # and the function(step==1), at last nextsymbol(step==2)
        funbody = []
        beginidx = 0
        endidx = len(filelist)
        target = funline
        step = 1
        if classname:
            step = 0
            target = classname
        for idx, val in enumerate(filelist):
            if step == 2:
                funbody.append(val)
                if target == val:
                    endidx = idx
                    break
            elif step == 1:
                if target == val:
                    beginidx = idx
                    funbody.append(val)
                    if not nextsymbol:
                        return beginidx, len(filelist)
                    target = nextsymbol
                    step = 2
            elif step == 0:
                if target == val:
                    target = funline
                    step = 1
        funindents = self.indentsOfSymbol(funline)
        if endidx != len(filelist):
            for i in range(0, len(funbody)):
                val = funbody.pop()
                if val and  self.indentsOfSymbol(val) < funindents:
                    return beginidx, (endidx - i)

    def update(self, fileLines, vallist):
        fileLines[self.posBegin:self.posEnd + 1] = vallist
        return "\n".join(fileLines)

    def operation(self):
        string = Decorator.operation(self)
        symbols = self.getSymbolOfFile(string)
        for key, val in paramsconf.substitutefunctionlist.items():
            fileLines = self.getLines(string)
            classline = None
            if not val[1]:
                funline = self.getGlobalFun(key, symbols)
            else:
                classline, funline = self.getAttributeOfClass(key,
                                                              val[1],
                                                              symbols)
            if not funline:
                logging.error("[ERROR] class %s is not found, "
                        "pless check you configure file", val[1])
            funidx = symbols.index(funline)
            nextsymbol, nextidx = self.findTheNextSymbol(funline,
                                                         funidx, symbols)
            self.posBegin, self.posEnd = self.positon(classline, funline,
                                                      nextsymbol, fileLines)
            vallist = self.getLines(val[0])
            if not vallist[len(vallist) - 1]:
                vallist.pop()
            if not vallist[0]:
                vallist.pop(0)
            string = self.update(fileLines, vallist)
            logging.info("[INFO] substitute function: %s", key)
        return string


class genClassMap(Decorator):

    def __init__(self, files):
        self.files = files

    def getKeyofClassName(self, name):
        return '_'.join(re.findall("[A-Z]+[^A-Z]*", name)).lower()

    def formatClassMap(self, mapName, rootClassMap={}):
        mapLine = "\n%s = {\n" % mapName
        if rootClassMap:
            rootClassKeyList = [key for key in rootClassMap.keys()]
            rootClassKeyList.sort()
            string = "\n".join(['%20s"%-31s: %s,' %
                                (' ', key + '"', rootClassMap[key])
                                for key in rootClassKeyList])

            string.rstrip(',')
        mapLine = mapLine + string
        mapLine = mapLine + '\n%16s}\n' % ' '
        return mapLine

    def getElemetFromTree(self, elements, elementDict, rootClass, exclude):
        for elementNode in elements:
            if (elementNode.nodeName == "xs:element" and
                not elementNode.getAttribute("type").startswith("xs:") and
                elementNode.getAttribute("type") not in exclude):
                key = elementNode.getAttribute("name")
                if (key in elementDict.keys()):
                    if (elementDict[key] in rootClass and
                        elementNode.getAttribute("type") in rootClass and
                        elementDict[key] != elementNode.getAttribute("type")):
                            logging.error("[ERROR] duplicate key, {%s: %s} "
                                          "already in _rootClassMap, "
                                          "skip {%s: %s}",
                                          key, elementDict[key],
                                          key, elementNode.getAttribute("type"))
                elif key:
                    elementDict[key] =  elementNode.getAttribute("type")
            children = elementNode.childNodes
            if children:
                self.getElemetFromTree(children, elementDict,
                                       rootClass, exclude)
    def getSimpleTypeFromTree(self, elements, typeList):
        for elementNode in elements:
            if elementNode.nodeName == "xs:simpleType":
                typeList.append(elementNode.getAttribute("name"))
            children = elementNode.childNodes
            if children:
                self.getSimpleTypeFromTree(children, typeList)

    def getElementDictFromSchema(self, schemaFile, symbols, exclude):
        rootClassList = self.rsdlRootClass(symbols)
        dom = xml.dom.minidom.parse(schemaFile)
        root = dom.documentElement

        simpleTypeList = []
        self.getSimpleTypeFromTree(root.childNodes, simpleTypeList)

        elementDict = {}
        self.getElemetFromTree(root.childNodes, elementDict,
                               rootClassList, exclude+simpleTypeList)
        if '' in elementDict.keys():
           elementDict.pop('')
        return elementDict

    def operation(self):
        string = Decorator.operation(self)
        symbols = self.getSymbolOfFile(string)
        logging.info("[INFO] append _rootClassMap in file %s",
                     self.files["target"])

        elementDict = self.getElementDictFromSchema(
                                       self.files["schema"],
                                       symbols,
                                       paramsconf.excludeInRootClassMap)

        formatLine = self.formatClassMap("_rootClassMap", elementDict)

        string = self.append(string, formatLine)
        return string

    def append(self, string, tailString):
        return  "\n".join([string, BEGINEGENERATE, tailString])


class appendFunction(Decorator):

    def __init__(self, files):
        self.files = files

    def operation(self):
        string = Decorator.operation(self)
        string = self.append(string, paramsconf.globalfunctionlist)
        logging.info("[INFO] append function at tail of %s",
                     self.files["target"])
        return string

    def append(self, string, tailString):
        tailString = "\n".join(tailString)
        return  "\n".join([string, tailString, ENDGENERATE])

def paramsHandle(schemaFile, paramsFile, paramsTmpFile, **kwargs):
    files = {}
    files["schema"] = schemaFile
    files["target"] = paramsFile
    files["tmp"] = paramsTmpFile
    if not 'log' in kwargs:
        files['log'] = LOGFILE
    else:
        files['log'] = kwargs['log']

    logConfigure(files['log'], 'debug')
    pcontext = paramsContext(files)

    # insert the import module
    md = addModule(files)
    md.setComponet(pcontext)

    # insert the an attribute of an class
    ca = addClassAttri(files)
    ca.setComponet(md)

    # substitute the function
    upfun = updataFunction(files)
    upfun.setComponet(ca)

    # append the _rootClassMap
    genMap = genClassMap(files)
    genMap.setComponet(upfun)

    # append the global function
    af = appendFunction(files)
    af.setComponet(genMap)
    contextString = af.operation()
    with open(files['target'], 'a') as f:
        f.write('%s' % contextString)

def main():
    genParser = CmdLineParser()
    genParser.handle_command(sys.argv[1:])
    outFile = genParser.getOutFile()
    # will support get the schema from the engine server
    # contextmanager.get('proxy').request('GET', '/api?schema')
    schemaFile = genParser.getSchemaFile()
    logFile = genParser.getLogFile()
    tmpOutFile = outFile + r".in"

    paramsHandle(schemaFile, outFile, tmpOutFile, log=logFile)


if __name__ == "__main__":
    main()
