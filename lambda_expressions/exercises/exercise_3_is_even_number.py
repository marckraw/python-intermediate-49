"""
IS EVEN NUMBER

Napisz funkcje lambda sprawdzającą czy dana liczba (integer) jest liczba parzystą. Przydatny bedzie
operator modulo (%).
"""
if __name__ == '__main__':
    is_even_number = lambda x: x % 2 == 0
    assert is_even_number(234)
    assert is_even_number(45) is False
