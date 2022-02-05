import json

from serialization.consts import JSON_FILE

if __name__ == '__main__':
    # load - wczytanie z pliku oraz deserializacja do obiektu pythonowego
    # loads - deserializacja do obiektu pythonowego

    with open(JSON_FILE) as in_file:
        data = json.load(in_file)

    for obj in data:
        print(obj)
        print(obj['imie'])
