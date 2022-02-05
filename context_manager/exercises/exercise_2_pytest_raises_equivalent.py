"""
PYTEST RAISES EQUIVALENT

Naszym zadaniem jest napisanie context managera imitującego zachowanie funkcji pytest.raises.
* W konstruktorze przyjmowane są 2 parametry: exception_type oraz opcjonalny match domyślnie None
* atrybut _exception_type - przyjmuje w konstruktorze typ wyjątku, który powinien wystąpić
* atrybut _match - oczekiwana wiadomość zawarta w wyjątku, na podstawie tej wartości będziemy
  sprawdzać czy wyjątek mial msg taki jak oczekiwany
* chcemy obsłuzyć przypadek gdy wyjątek nie wystąpi, wtedy AssertionError
* chcemy obsłużyc przypadek gdy wyjątek który wystąpił nie jest wyjątkiem ktorego oczekiwaliśmy, wtedy AssertionError
* chcemy obsłużyć sytuacje gdy oczekiwana wiadomość nie jest równa rzeczywistej ktora przyszla z wyjatkiem.
  Oczywiscie pamietamy ze match jest opcjonalne, wiec gdy jest rowne None to nie sprawdzamy czy wiadomości się zgadzaja.
  W razie wystapienia niezgodności to AssertionError.

* TIP: aby w __exit__() na koniec wykonania metody nie byl rzucany wyjątek należy na samym końcu
       metody zwrócić True

"""
import pytest


class PytestRaisesEquivalent:

    def __init__(self, exception_type, match=None):
        self._exception_type = exception_type
        self._match = match

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # algebra boola
        # if exc_type is None:
        if not exc_type:
            raise AssertionError
        if self._exception_type is not exc_type:
            raise AssertionError
        if self._match and self._match is not str(exc_val):
            raise AssertionError
        return True


def func(param):
    if param < 0:
        raise ValueError('Ala ma kota')


if __name__ == '__main__':
    with PytestRaisesEquivalent(NotImplementedError, match='test msg'):
        raise NotImplementedError('test msga')

    with pytest.raises(ValueError, match='Ala ma kota'):
        func(-1)
