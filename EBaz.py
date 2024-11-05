from enum import Enum


class EBaz(Enum):
    Baz1 = ()
    Baz2 = ()
    Baz3 = ()

    def __new__(cls):
        newObject = object.__new__(cls)
        return newObject
