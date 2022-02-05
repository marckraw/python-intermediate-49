from dataclasses import dataclass, field, InitVar
from typing import List

from object_oriented_programming.abstract import Figura


# documentation: https://docs.python.org/3/library/dataclasses.html

@dataclass
class Prostokat(Figura):
    a: int
    b: int

    # available types here: https://www.python.org/dev/peps/pep-0526/

    def obwod(self) -> float:
        return 2 * (self.a + self.b)

    def pole(self) -> float:
        return self.a * self.b


# to samo tylko bez @dataclass
# class Prostokat(Figura):
#     def __init__(self, a: int, b: int, color: str):
#         super().__init__(color)
#         self.a = a
#         self.b = b
#
    # def __repr__(self) -> str:
    #     return f"Prostokat(a={self.a}, b={self.b})"
#
#     def __eq__(self, other) -> bool:
#         return isinstance(other, Prostokat) and (self.a, self.b) == (other.a, other.b)
#
#     def obwod(self) -> float:
#         return 2 * (self.a + self.b)
#
#     def pole(self) -> float:
#         return self.a * self.b

@dataclass
class Sample:
    sample_int: int
    sample_list_of_ints: List[int]

    sample_not_in_repl_int: int = field(repr=False)
    # or
    # sample_not_in_repl_int: InitVar[int]

    sample_default_int: int = field(default=10)
    sample_calculated_int: int = field(init=False)

    def __post_init__(self):
        self.sample_calculated_int = self.sample_int * 20


if __name__ == '__main__':
    # p1 = Prostokat(3, 4)
    # p2 = Prostokat(3, 4)
    # print(p1)
    # print(p1 == p2)
    sample = Sample(
        sample_int=2,
        sample_list_of_ints=[1, 2, 3],
        sample_not_in_repl_int=999,
    )
    print(sample)
    t=0