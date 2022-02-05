def dummy_func():
    a = 3
    b = [1, 0, 2]
    for elem in b:
        try:
            wynik = a / elem
        except ZeroDivisionError as exp:
            print(str(exp))
            # print('Pamietaj cholero nie dziel przez zero')
            continue
            # raise ValueError(str(exp))
            # wynik = 'Pamietaj cholero nie dziel przez zero'
        print(f"Wynik to: {wynik}")



# class MyClass:
#     def __str__(self):
#         return 'ALa ma kota'
#
#
# obj = MyClass()
# print(str(obj))
#
if __name__ == '__main__':
    dummy_func()
