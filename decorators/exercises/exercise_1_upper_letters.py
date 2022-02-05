"""
UPPER LETTERS

Naszym zadaniem jest napisanie dekoratora to_uppercase, który charakteryzować się będzie
działaniem takim, że dla każdej udekorowanej funkcji zwracającej stringa będzie on modyfikował
zwracaną wartość poprzez jej zmiane na duże litery.
Do przetestowania tego dekoratora została utworzona funkcja, która na podstawie stringa
przychodzącego w parametrze zmienia jego wartość na taką, gdzie każda litera jest oddzielona od
siebie spacją.
* musimy pamiętać, że nasza funkcja przymuje parametr, więc nasz dekorator również powinien
  umożliwić przesłanie parametru do tej funkcji
* w dekoratorze warto najpierw wykonać udekorowaną funkcje, po czym dopiero dzialac na jej
  wartości zwróconej

ROZWINIECIE:
Jako rozwinięcie dodajmy kolejny dekorator include_length. Ten dekorator bedzie takze zliczac
dlugosc stringa zwracanego przez udekorowana funkcje (wystarczy uzyc na stringu len()). Ten
dekorator modyfikuje wartość zwracaną przez udekorowaną funkcje i zwraca ją w postaci krotki.
                                (<len>, <rezultat_funcji>)

Chcemy doprowadzić do takiej sytuacji, gdzie wykorzystamy oba dekoratory na raz na jednej funkcji.
"""


def to_uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


def include_length(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return (len(result), result)


@include_length
@to_uppercase
def scatter_string(string):
    return " ".join(string)


if __name__ == '__main__':
    # 'hello' -> 'h e l l o' -> 'H E L L O' -**> (9, 'H E L L O')
    #    |           |              |                   |
    # parametr   wynik func    wynik func po @     wynik po @*
    assert scatter_string('hello') == 'H E L L O'
    # assert scatter_string('hello') == (9, 'H E L L O')
