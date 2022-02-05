"""
INDEX GENERATOR

Naszym zadaniem jest napisanie generatora indexow, z ktorego beda korzystaly kolejno tworzone konta.
W tym celu uzupelnij cialo generatora index_generator.
* pamietaj o uzyciu slowka kluczowego 'yield' do zwrocenia wartosci
* na poczatku index powinien byc rowny 0
* przy kazdym nastepnym uzyciu generatora zwracany jest indeks o jeden wiekszy niz poprzednim razem

"""


def index_generator():
    index = 0
    while True:
        yield index
        index += 1


index_generator_instance = index_generator()


class Account:

    def __init__(self, username: str, password: str, _id=None):
        self.username = username
        self.password = password
        self.id = _id if _id else next(index_generator_instance)
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

    array = []
    for _ in range(10):
        array.append(Account(username='sample_username', password='sample_password'))


    a = [1, 2, 3, 4, 5]
    *_, four, five = a

    expected_id = 0
    for account in accounts:
        assert account.id == expected_id
        expected_id += 1
