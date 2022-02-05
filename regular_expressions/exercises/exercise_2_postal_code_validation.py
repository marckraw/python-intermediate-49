"""
POSTAL CODE VALIDATION

Naszym zadaniem jest napisanie funkcji korzystajacej z wyrazenia regularnego, ktora podda walidacji
kod pocztowy przyjmowany w parametrze. Kod pocztowy sklada sie z 2 cyfr, myślnika i 3 cyfr.
"""

import re


def postal_code_validation(postal_code):
    return bool(re.search(r'^[0-9]{2}-[0-9]{3}$', postal_code))


if __name__ == '__main__':
    assert postal_code_validation('43-123')
    assert postal_code_validation('00-000')
    assert not postal_code_validation('0-000')
    assert not postal_code_validation('00-00')
    assert not postal_code_validation('000-00')
