#!/usr/bin/python
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

from codegen.xsd.xsdcodegen import XsdCodegen
from codegen.rsdl.rsdlcodegen import RsdlCodegen
from ovirtsdk.api import API

SERVER = 'http://localhost:8700'
USER = 'admin@internal'
PASSWORD = 'letmein!'

if __name__ == "__main__":

    # create api proxy
    api = API(url=SERVER, username=USER, password=PASSWORD)

    # generate python2xml bindings
    XsdCodegen(api).generate()

    # generate resources brokers
    RsdlCodegen(api).generate()
