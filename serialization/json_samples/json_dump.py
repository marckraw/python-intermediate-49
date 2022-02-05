import json

from serialization.consts import JSON_FILE

kursanci = [
    {
        'imie': "Adam",
        'nazwisko': "Brzeczyszczykiewicz",
        'liczba punktow': 20
    },
    {
        'imie': "Janusz",
        'nazwisko': "Smuga",
        'liczba punktow': 18
    }
]

if __name__ == '__main__':
    # dump - serializacja i zapis do pliku
    # dumps - serializacja

    with open(JSON_FILE, 'w') as out_file:
        json.dump(kursanci, out_file, indent=2)
