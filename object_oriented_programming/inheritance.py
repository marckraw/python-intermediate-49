class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        super().__init__(imie, wiek)
        # Osoba.__init__(self, imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        super().__init__(imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


if __name__ == '__main__':
    os1 = Osoba("Henryk", 54)
    os2 = Pracownik("Jacek", 36, 20, 160)
    os3 = Student("Agata", 22, 1000)

    people = [os2, os3]
    for person in people:
        print(person.pokaz_finanse())

    print(os1)
    print(os2)
    print(os3)
