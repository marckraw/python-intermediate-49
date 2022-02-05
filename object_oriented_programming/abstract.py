from abc import ABC, abstractmethod
from math import pi
from typing import List


class Figura(ABC):

    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def obwod(self) -> float:
        pass

    @abstractmethod
    def pole(self) -> float:
        pass

    def show_color(self):
        print(self.color)


class Prostokat(Figura):
    def __init__(self, color: str, a: float, b: float):
        super().__init__(color)
        self.a = a
        self.b = b

    def obwod(self) -> float:
        return 2 * (self.a + self.b)

    def pole(self) -> float:
        return self.a * self.b


class Kolo(Figura):
    def __init__(self, color: str, r: float):
        super().__init__(color)
        self.r = r

    def obwod(self) -> float:
        return 2 * self.r * pi

    def pole(self) -> float:
        return pi * self.r ** 2


class Kwadrat(Figura):
    def __init__(self, color: str, a: float):
        super().__init__(color)
        self.a = a

    def obwod(self) -> float:
        return 4 * self.a

    def pole(self) -> float:
        return self.a * self.a


def sum_figures_circuit(figures: List[Figura]):
    sum = 0
    for figure in figures:
        sum += figure.obwod()

    return sum


if __name__ == '__main__':
    prostokat = Prostokat('Pink', 3, 5)
    kolo = Kolo('Red', 12)
    kwadrat = Kwadrat('Blue', 5)

    figure_list = [
        prostokat,
        kolo,
        kwadrat,
    ]

    result = sum_figures_circuit(figure_list)
    print(result)
