from ICorge import ICorge
from IFoo import IFoo


class Corge(ICorge):
    __foo: IFoo

    @property
    def Foo(self):
        pass
