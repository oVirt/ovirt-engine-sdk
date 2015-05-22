
try:
    from UserDict import UserDict
except ImportError:
    from collections import UserDict

try:
    import thread
except ImportError:
    import _thread as thread

class OrderedDict(UserDict):
    """A dictionary preserving insert order"""
    def __init__(self, dict=None):
        self._keys = []
        self.__plock = thread.allocate_lock()
        self.__rlock = thread.allocate_lock()

        UserDict.__init__(self, dict)

    def clear(self):
        """Clears the dictionary"""
        with self.__plock:
            UserDict.clear(self)
            self._keys = []

    def copy(self):
        """Copying dictionary"""
        dict = UserDict.copy(self)
        dict._keys = self._keys[:]
        return dict

    def popitem(self):
        """Pops last item from the dictionary"""
        with self.__plock:
            if len(self._keys) == 0:
                raise KeyError('Empty')

            key = self._keys[-1]
            val = self[key]
            del self[key]

            return (key, val)

    def setdefault(self, key, failobj=None):
        """Sets default for dict items"""
        with self.__plock:
            if key not in self._keys:
                self._keys.append(key)
            return UserDict.setdefault(self, key, failobj)

    def update(self, dict):
        """Updates dictionary with new items"""
        with self.__rlock:
            UserDict.update(self, dict)
            for key in dict.keys():
                if key not in self._keys:
                    self._keys.append(key)

    def __delitem__(self, key):
        with self.__plock:
            UserDict.__delitem__(self, key)
            self._keys.remove(key)

    def __setitem__(self, key, item):
        with self.__plock:
            UserDict.__setitem__(self, key, item)
            if key not in self._keys:
                self._keys.append(key)

    def values(self):
        """Returns values in a same order they where inserted"""
        with self.__plock:
            return map(self.get, self._keys)

    def items(self):
        """Returns items in a same order they where inserted"""
        with self.__plock:
            return map(lambda key: (key, self[key]), self._keys)

    def keys(self):
        """Returns keys in a same order they where inserted"""
        with self.__plock:
            return self._keys[:]
