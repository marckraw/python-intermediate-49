"""
INDEX ITERATOR

Naszym zadaniem jest napisanie iteratora generującego indexy, z ktorego beda korzystaly kolejno
tworzone konta.
W tym celu uzupelnij cialo iteratora IndexIterator.
* __iter__ zawsze zwraca instancje obiektu, czyli 'return self'
* w __init__ zdefiniuj poczatkowa wartosc indexu - 0
* przy kazdym nastepnym uzyciu iteratora zwracany jest indeks o jeden wiekszy niz poprzednim razem
* w __next__ musimy zwracac wartość indeksu oraz go inkrementowac, aby nastepnym razem użyć juz
  większego indeksu

"""


class IndexIterator:

    def __init__(self):
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # self._index += 1
        # return self._index
        current_index = self._index
        self._index += 1
        return current_index

index_iterator = IndexIterator()


class Account:

    def __init__(self, username: str, password: str, _id=None):
        self.username = username
        self.password = password
        self.id = _id if _id else next(index_iterator)

        # if _id:
        #     self.id = _id
        # else:
        #     self.id = next(index_iterator)

if __name__ == '__main__':
    accounts = [
        Account(username='sample_username', password='sample_password')
        for _
        in range(10)
    ]

    expected_id = 0
    for account in accounts:
        assert account.id == expected_id
        expected_id += 1

    # account1 = Account('pwiener', '123qweASD')  # id = 1
    # account2 = Account('majster', 'alamakota')  # id = 2
