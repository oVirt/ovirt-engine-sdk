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

class StringUtils(object):
    '''
    Providing string formating services
    '''
    PLURAL_SUFFIX = 's'

    @staticmethod
    def toSingular(candidate, exceptions=[]):
        '''
        Converts string to singular form
        
        @param candidate: string to convert
        @param exceptions: plural form exceptions
        '''
        if candidate and candidate.endswith(StringUtils.PLURAL_SUFFIX) \
                and candidate not in exceptions:
            return candidate[0:len(candidate) - 1]
        return candidate

    @staticmethod
    def toPlural(candidate):
        '''
        Converts string to plural form
        
        @param candidate: string to convert
        '''
        if candidate and not candidate.endswith(StringUtils.PLURAL_SUFFIX):
            return candidate + StringUtils.PLURAL_SUFFIX
        return candidate
