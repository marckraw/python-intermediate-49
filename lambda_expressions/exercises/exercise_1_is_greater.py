"""
IS GREATER

Napisz lambda ktora przyjmuje dwa argumenty i sprawdza czy pierwszy z nich jest wiekszy od
drugiego. Funkcja zwraca boola.
"""
if __name__ == '__main__':
    is_greater = lambda x, y: x > y
    print(is_greater(3, 2))
    print(is_greater(2, 3))
