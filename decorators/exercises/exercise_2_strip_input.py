"""
STRIP INPUT

Naszym zadaniem jest napisanie dekoratora strip_input_decorator, ktorego dzialaniem bedzie
odpowiednie przygotowanie danych wejściowy dla funkcji pobierającej dane uzytkownika z
"bazy danych". Takie przygotowanie zakłada usunięcie białych znaków na początku i końcu
przychodzacego stringa (strip()) oraz zastąpienie w wszystkich spacji wewnątrz stringa znakiem '_'.
* w dekoratorze przygotowanie danych nalezy przeprowadzic przed wywołaniem funkcji udekorowanej
* <str>.replace(<wartosc_do_zastapienia>, <zemiennik>)
* <str>.strip()
"""
USER_DATA = {
    'id': 1,
    'read_books': ['Harry Potter', 'Lord of the Rings', 'Dune'],
    'favorite_pet': 'dog',
    'number_of_children': 4,
}


def strip_input_decorator(func):
    def wrapper(user_input):
        user_input_result = user_input.strip().replace(' ', '_')

        return func(user_input_result)

    return wrapper


@strip_input_decorator
def get_user_data(user_input):
    return USER_DATA[user_input]


if __name__ == '__main__':
    assert get_user_data(user_input='id') == 1
    assert get_user_data('read books   ') == ['Harry Potter', 'Lord of the Rings', 'Dune']
    assert get_user_data('favorite pet  ') == 'dog'
    assert get_user_data('  number_of_children') == 4
