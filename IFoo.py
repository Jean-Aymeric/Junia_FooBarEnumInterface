from abc import ABC, abstractmethod

from EBaz import EBaz
from ICorge import ICorge


class IFoo(ABC):
    @abstractmethod
    def addBaz(self, baz: EBaz):
        pass

    @abstractmethod
    @property
    def Corge(self):
        pass

    @abstractmethod
    @Corge.setter
    def Corge(self, icorge: ICorge):
        pass
