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


import datetime

#============================================================
#==========================IMPORTS===========================
#============================================================

intro = \
        "#\n" + \
        "# Copyright (c) 2010 Red Hat, Inc.\n" + \
        "#\n" + \
        "# Licensed under the Apache License, Version 2.0 (the \"License\");\n" + \
        "# you may not use this file except in compliance with the License.\n" + \
        "# You may obtain a copy of the License at\n" + \
        "#\n" + \
        "#           http://www.apache.org/licenses/LICENSE-2.0\n" + \
        "#\n" + \
        "# Unless required by applicable law or agreed to in writing, software\n" + \
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n" + \
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n" + \
        "# See the License for the specific language governing permissions and\n" + \
        "# limitations under the License.\n" + \
        "#\n" + \
        "\n\n########################################\n" + \
        "############ GENERATED CODE ############\n" + \
        "########################################\n\n"

stamp = \
"'''Generated at: " + str(datetime.datetime.now()) + "'''\n\n"

imports = intro + stamp + \
"from ovirtsdk.xml import params\n" + \
"from ovirtsdk.utils.urlhelper import UrlHelper\n" + \
"from ovirtsdk.utils.filterhelper import FilterHelper\n" + \
"from ovirtsdk.utils.parsehelper import ParseHelper\n" + \
"from ovirtsdk.utils.searchhelper import SearchHelper\n" + \
"from ovirtsdk.infrastructure.common import Base\n" + \
"from ovirtsdk.infrastructure.context import context\n" + \
"from ovirtsdk.infrastructure.errors import MissingParametersError\n" + \
"from ovirtsdk.infrastructure.errors import DisconnectedError\n" + \
"from ovirtsdk.infrastructure.errors import RequestError\n\n\n"

class Import(object):
    @staticmethod
    def getimports(): return imports
