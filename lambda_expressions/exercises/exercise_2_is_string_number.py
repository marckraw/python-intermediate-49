"""
IS STRING NUMBER

Napisz funkcje lambda przyjmujaca jako argument string. Funkcja ma sprawdzic czy dany string jest
numerem, czyli czy zawiera tylko cyfry. Do tego posluz sie metoda stringa <str>.isdigit().
"""
if __name__ == '__main__':
    is_string_number = lambda x: x.isdigit()
    assert is_string_number('123')
    assert not is_string_number('Ala ma kota')
