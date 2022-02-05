"""
VEHICLES

1. Abstract classes
Naszym zadaniem przy uzyciu odpowiedniej abstracji napisanie kilku klas. Będziemy budować
hierarchię zależności kilku wybranych środków transportów, zarówno lądowych jak i wodnych.
1.1. class Vehicle:
    * klasa ABSTRAKCYJNA
    * posiada tylko jedną metodę abstrakcyjną get_current_speed
1.2 klasa LandVehicle:
    * dziedziczy po klasie Vehicle
    * jest również klasą abstrakcyjną
    * w konstruktorze przyjmuje parametr wheels_number, który zapisywany do ochronionego atrybutu
      _wheels_number
    * klasa posiada także abstrakcyjną metodę drive
1.3 klasa WaterVehicle:
    * dziedziczy po klasie Vehicle
    * jest również klasą abstrakcyjną
    * w konstruktorze przyjmuje parametry name oraz propulsion_type; zapisywane są one do
      chronionych atrybutów
    * posiada abstrakcyjną metodę swim
1.4 klasa Car:
    * dziedziczy po klasie LandVehicle;
    * NIE jest klasą abstrakcyjną!
    * implementuje odziedziczone metod; każda z metod powinna wyświetlać jakąś wiadomość;
      można sobie wybrać treść (nie jest to istotne)
1.5 klasa Ship:
    * dziedziczy po klasie WaterVehicle;
    * NIE jest klasą abstrakcyjną!
    * implementuje odziedziczone metod; każda z metod powinna wyświetlać jakąś wiadomość;
      można sobie wybrać treść (nie jest to istotne)

2. Multiple inheritence
Wyobraźmy sobie taką sytuację, że chcemy dodać amfibię. W jaki sposób rozwiążemy dziedziczenie?
Należy napisać klasę AmphibiousVehicle w taki sposób, aby ten pojazd mógł zarówno poruszać się po
lądzie jak i po wodzie. Zaimplementuj wszystkie odziedziczone metody. W konstruktorze wskaż w
jakiej kolejności powinny się wykonać konstruktory klas, po których dziedziczy.

"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_current_speed(self) -> float:
        pass


class LandVehicle(Vehicle, ABC):
    def __init__(self, wheels_number: int):
        _wheels_number = wheels_number

    @abstractmethod
    def drive(self) -> str:
        pass


class WaterVehicle(Vehicle, ABC):
    def __init__(self, name: str, propulsion_type: str):
        _name = name
        _propulsion_type = propulsion_type

    @abstractmethod
    def swim(self) -> str:
        pass


class Car(LandVehicle):
    def drive(self):
        print(f"Jade z predkoscia {self.get_current_speed()}")

    def get_current_speed(self):
        return 120


class Ship(WaterVehicle):
    def __init__(self, name, propulsion_type):
        super().__init__(name, propulsion_type)

    def swim(self):
        print(f"Plyne z predkoscia {self.get_current_speed()}")

    def get_current_speed(self):
        return 50


class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, wheels_number, name, propultion_type):
        LandVehicle.__init__(self, wheels_number)
        WaterVehicle.__init__(self, name, propultion_type)

    def drive(self) -> str:
        print(f"Jade amfibia z predkoscia {self.get_current_speed()}")

    def swim(self) -> str:
        print(f"Plyne amfibia z predkoscia {self.get_current_speed()}")

    def get_current_speed(self):
        return 300


if __name__ == '__main__':
    car = Car(wheels_number=4)
    ship = Ship(name='Nugat', propulsion_type='asd')
    print(car.get_current_speed())
    car.drive()
    print(ship.get_current_speed())
    ship.swim()

    print()
    print()

    amfibia = AmphibiousVehicle(wheels_number=4, name="Amfibia", propultion_type='some weird one')
    print(amfibia.get_current_speed())
    amfibia.drive()
    amfibia.swim()
