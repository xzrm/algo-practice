from typing import Protocol

class Base(Protocol):

    def m1(self, i: int) -> int:
        ...

    def m2(self, s: str) -> str:
        ...

class C:

    def m1(self, i: int) -> int:
        return i


    def m2(self, s: str) -> str:
        return s


class M:
    
    def m1(self, b: Base, v: int) -> None:
        print (b.m1(v))


c = C()
m = M()
m.m1(c, 5)
