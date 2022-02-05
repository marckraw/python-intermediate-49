"""
AVERAGE SALARY

Naszym zadaniem jest napisanie funkcji, która policzy średnią zarobków odczytanych z wskazanego
pliku csv. Funkcja przyjmuje także index kolumny, pod którą znajdują się zarobki pracowników.
Zaleca się skorzystanie z pliku serialization\assets\data.csv, z którego korzystaliśmy już
wcześniej.

* należy otworzyć plik i za pomocą csv.reader czytać zawartość pliku linijka po linijce.
* zauważmy, że pierwsza linijka pliku to nagłówki kolumn, które trzeba pominąć przy zliczaniu
  zarobków. Aby tego dokonać posłuż się funkcją next()
* w dalszej cześci należy w pętli sumować wysokości zarobków wszystkich pracowników
* dodatkowo musimy liczyć ile tych pracowników jest, ponieważ csv.reader nie dotarcza nam
  informacji o liczbie danych w pliku
* na samym końcu (już poza blokiem with) przeprowadzamy działanie wyliczające średnią zarobków
* wynik zwracamy z funkcji
"""

import csv

from serialization.consts import CSV_FILE


def average_salary(filepath, index):
    salary_sum = 0
    salary_amount = 0

    with open(filepath) as in_file:
        reader = csv.reader(in_file)
        next(reader)

        for row in reader:
            print(row[1])
            salary_sum += float(row[1])
            salary_amount += 1


    return salary_sum / salary_amount


if __name__ == '__main__':
    average = average_salary(CSV_FILE, 1)
    print()
    print(average)
