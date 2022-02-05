class CustomException(Exception):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.msg = kwargs.get('msg')


def dummy_func():
    a = 3
    b = [1, 0, 2]
    for elem in b:
        if elem == 0:
            raise CustomException("Dzielnik nie może być równy zeru", msg='ALa ma kota')
        wynik = a / elem
        print(f"Wynik to: {wynik}")


if __name__ == '__main__':
    dummy_func()
