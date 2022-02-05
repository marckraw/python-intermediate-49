from abc import ABC, abstractmethod


class Osoba(ABC):
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"

    @abstractmethod
    def pokaz_finanse(self):
        pass


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        Osoba.__init__(self, imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        Osoba.__init__(self, imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


class PracujacyStudent(Pracownik, Student):
    def __init__(self, imie, wiek, stawka, liczba_godzin, stypendium):
        Pracownik.__init__(self, imie, wiek, stawka, liczba_godzin)
        Student.__init__(self, imie, wiek, stypendium)

    def pokaz_finanse(self):
        # MRO - Method Resolution Order
        # return self.stawka * self.liczba_godzin + self.stypendium
        return Pracownik.pokaz_finanse(self) + Student.pokaz_finanse(self)


if __name__ == '__main__':
    # os1 = Osoba("Henryk", 54)
    os2 = Pracownik("Jacek", 36, 20, 160)
    os3 = Student("Agata", 22, 1000)
    os4 = PracujacyStudent("Monika", 24, 9.5, 70, 550)
    # print(os1)
    print(os2)
    print(os3)
    print(os4)
    print(os4.pokaz_finanse())
