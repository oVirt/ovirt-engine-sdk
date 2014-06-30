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
    def toSingular(candidate, exceptions={}):
        '''
        Converts string to singular form
        
        @param candidate: string to convert
        @param exceptions: plural form exceptions
        '''
        if candidate is None:
            return None
        if candidate in exceptions:
            return exceptions[candidate]
        if candidate.endswith(StringUtils.PLURAL_SUFFIX):
            return candidate[:-1]
        return candidate

    @staticmethod
    def toPlural(candidate, exceptions={}):
        '''
        Converts string to plural form
        
        @param candidate: string to convert
        @param exceptions: plural form exceptions
        '''
        if candidate is None:
            return None
        for plural, singular in exceptions.iteritems():
            if candidate == singular:
                return plural
        if not candidate.endswith(StringUtils.PLURAL_SUFFIX):
            return candidate + StringUtils.PLURAL_SUFFIX
        return candidate
