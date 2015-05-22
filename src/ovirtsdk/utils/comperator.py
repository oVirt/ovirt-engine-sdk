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
import inspect
import types

class Comparator(object):
    '''
    Provides object deep comparison capabilities
    '''

    @staticmethod
    def compare(obj1, obj2, callback=None):
        '''
        Auditable deep compare of obj1, obj2

        @param callback: method to invoke on != prop, format: callback(arg)
        @return: True|False

        @attention: does not treat infinite loops caused when objX has objY which has objX inside.
        '''

        try:
            if not (callback or hasattr(callback, '__call__')):
                return (isinstance(obj2, obj1.__class__)
                    and obj1.__dict__ == obj2.__dict__)
            else:
                if not (inspect.isclass(type(obj1)) and inspect.isclass(type(obj2))):
                    return obj1 == obj2
                else:
                    if isinstance(obj2, obj1.__class__):
                        for key, value in obj1.__dict__.iteritems():

                            #do not compare methods and private fields
                            if (isinstance(value, types.FunctionType) or
                                    key.startswith("__")):
                                continue

                            #prop not in dict
                            if key not in obj2.__dict__:
                                callback(key)
                                return False

                            #value1 != value2
                            if obj2.__dict__[key] != value:
                                callback(key)
                                return False

                        return True
                    else:
                        return False
        except RuntimeError:
            print('%s object comparison caused infinite loop.' % type(obj1).__name__)
