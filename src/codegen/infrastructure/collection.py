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


class Collection(object):
    '''
    The Collection data holder
    '''
    def __init__(self, name, body):
        self.name = name
        self.body = body
        # methods{name:body}
        self.methods = {}
        self.resource = None

    def getResource(self):
        return self.resource

    def setResource(self, value):
        self.resource = value

    def hasResource(self, value):
        return self.resource is not None

    def addMethod(self, name, body):
        self.methods[name] = body

    def hasMethod(self, name):
        return self.methods.has_key(name)

    def getMethod(self, name):
        if self.hasMethod(name):
            return self.methods[name]
        return None
