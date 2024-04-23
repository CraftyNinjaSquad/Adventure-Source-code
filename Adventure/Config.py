"""This is just a file to store specific data like
what room the player is currently in, if they have
certain items, or how much health they have left.
I felt it would be easier and better organized if
it was like this."""


class room:
    def __init__(self, room = ""):
        self._room = room

    def get_room(self):
        return self._room

    def set_room(self, x):
        self._room = x

class hasKey1:
    def __init__(self, key1 = False):
        self._key1 = key1

    def get_key1(self):
        return self._key1

    def set_key1(self, x):
        self._key1= x

class hasKey2:
    def __init__(self, key2 = False):
        self._key2 = key2

    def get_key2(self):
        return self._key2

    def set_key2(self, x):
        self._key2 = x

class hasKey3:
    def __init__(self, key3 = False):
        self._key3 = key3

    def get_key3(self):
        return self._key3

    def set_key3(self, x):
        self._key3 = x

class hasBow:
    def __init__(self, bow = False):
        self._bow = bow

    def get_bow(self):
        return self._bow

    def set_bow(self, x):
        self._bow = x

