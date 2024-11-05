from abc import ABC, abstractmethod

from IFoo import IFoo


class ICorge(ABC):
    @abstractmethod
    @property
    def Foo(self):
        pass

    @abstractmethod
    @Foo.setter
    def Foo(self, ifoo: IFoo):
        pass
