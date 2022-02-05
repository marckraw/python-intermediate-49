from datetime import datetime


def run_only_between(from_=7, to_=22):
    # dekorator, który wywołuje udekorowaną funkcję tylko w określonych godzinach
    def dec(func):
        def wrapper():
            if from_ <= datetime.now().hour < to_:
                func()

        return wrapper

    return dec


@run_only_between(10, 20)
def say_something():
    print("Hello world")


if __name__ == '__main__':
    say_something()
