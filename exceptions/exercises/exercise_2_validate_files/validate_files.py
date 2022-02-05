"""
VALIDATE FILES

Naszym zadaniem jest napisanie logiki odpowiedzialnej za sprawdzenie czy dane w podanych plikach
są w poprawnym formacie. Jako poprawny format uznaje się tylko i wyłącznie następujące:

                            <nazwa_przepisu>;<link>

Nasza funkcjonalność powinna zawierać wyświetlnie informacji o liczbie plików posiadających błędy.
Należy użyć funkcji read_files() z poprzedniego zadania.


--- validate_files ---
* jako parametr przyjmuje listę ścieżek do plików (podobnie jak w poprzednim zadaniu)
* odczytuje zawartość podanych plików za pomocą read_files()
* wywołuje operacje walidacji na danych z każdego pliku
* na koniec wyświetla informację i liczbie zanalezionych błędów

--- validate_content ---
* funkcja przeprowadzająca walidację na przychodzących danych z jednego pliku
* jako parametr przyjmuje dane z jednego pliku w postaci listy stringów
* jeżeli dana linia nie odpowiada przyjętemu przez na formatowi to rzucany jest utworzony przez nas
  wyjącek FileParsingError
** dodatkowy akceptowalny przypadek linii to taki gdzie jest ona pusta
** należy pamiętać o usuwaniu znaków nowej linii '\n'
** przydatne metody stringa w tym zadaniu: replace(), split()
"""

# strip()

import os

from exceptions.exercises.exercise_1_read_files.read_files import read_files, PATHS, read_file

FILES = PATHS


class FileParsingError(Exception):
    pass


def validate_content(file_content):
    for line in file_content:
        parsed_line = line \
            .strip() \
            .split(';')

        if (len(parsed_line) != 2 or parsed_line[-1] == '') or (len(parsed_line) == 1 and parsed_line[0] == ''):
            raise FileParsingError

        print(parsed_line)


def validate_files(files):
    errors_amount = 0
    files_content = read_files(files)

    for file_content in files_content:
        try:
            validate_content(files_content=file_content)
        except FileParsingError:
            errors_amount += 1

    return errors_amount


if __name__ == '__main__':
    parsing_errors_in_files = validate_files(files=FILES)
    print(parsing_errors_in_files)

