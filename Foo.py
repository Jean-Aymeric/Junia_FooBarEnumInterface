from EBaz import EBaz
from IBar import IBar
from ICorge import ICorge
from IFoo import IFoo
from IQux import IQux
from Qux import Qux


class Foo(IFoo):
    __bar: IBar
    __bazs: list[EBaz]
    __qux: IQux
    __corge: ICorge | None

    def __init__(self, bar: IBar):
        self.__bar = bar
        self.__bazs = []
        self.__qux = Qux()
        self.__corge = None

    def addBaz(self, baz: EBaz):
        self.__bazs.append(baz)

    @property
    def Corge(self):
        return self.__corge

    @Corge.setter
    def Corge(self, icorge: ICorge):
        self.__corge = icorge
