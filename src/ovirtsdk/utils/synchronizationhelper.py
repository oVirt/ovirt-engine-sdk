#
# Copyright (c) 2013 Red Hat Inc.
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


########################################
############ GENERATED CODE ############
########################################


import threading

def synchronized(function):
    """
    Synchronizes the function
    """
    return __usinglock(threading.RLock())(function)

def __usinglock(lock):
    def decorator(function):
        body = __tryexecute(lock.release)(function)
        def execute(*args, **kwargs):
            lock.acquire()
            return body(*args, **kwargs)
        return execute
    return decorator

def __tryexecute(finallyf):
    def decorator(invokeable):
        def execute(*args, **kwargs):
            try: result = invokeable(*args, **kwargs)
            finally: finallyf()
            return result
        return execute
    return decorator
