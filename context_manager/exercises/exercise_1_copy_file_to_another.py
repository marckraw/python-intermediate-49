"""
COPY FILE TO ANOTHER

Naszym zadaniem jest napisanie funkcji kopiującej dane z jednego pliku do drugiego.

* parametr src_file - ścieżka do pliku, z którego będziemy kopiować dane
* parametr destination_file - ścieżka do pliku, do którego będziemy kopiować dane (może to być nieistniejący plik)
* zaleca się otworzyć pierwszy plik, przypisać dane do zmiennej, otworzyć drugi plik i zapisać w nim dane
* OBOWIAZKOWO: uzyc context managera 'with'
"""

import os


def copy(src_file: str, destination_file: str):
    with open(src_file, 'r') as f:
        data = f.read()
    with open(destination_file, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    exercises_path = os.path.dirname(__file__)
    src_file = os.path.join(exercises_path, 'assets', 'file-to-copy.txt')
    destination_file = os.path.join(exercises_path, 'assets', 'copied-file.txt')
    copy(
        src_file=src_file,
        destination_file=destination_file,
    )
