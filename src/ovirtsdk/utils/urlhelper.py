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

class UrlHelper(object):
    @staticmethod
    def replace(url, args={}):
        for k, v in args.items():
            url = url.replace(k, v)
        return url

    @staticmethod
    def append(url, urlparam):
        if urlparam:
            return url + '/' + urlparam
        return url
