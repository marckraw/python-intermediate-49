def decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')

    return wrapper


@decorator
def sample_func1():
    print('Hello World')


# ekwiwalent dekoratora
# sample_func1 = decorator(sample_func1)


def parametrized_decorator(before_msg, after_msg):
    def decorator(func):
        def wrapper():
            print(before_msg)
            func()
            print(after_msg)

        return wrapper

    return decorator


@parametrized_decorator('Parametrized before', 'Parametrized after')
def sample_func2():
    print('Hello World')


@parametrized_decorator('Parametrized before', 'Parametrized after')
@decorator
def sample_func3():
    print('Hello World')


def decorator_func_with_params(func):
    def wrapper(*args, **kwargs):
        print('Before')
        func(*args, **kwargs)
        print('After')

    return wrapper


# func = parametrized_decorator('Parametrized before', 'Parametrized after')
# sample_func3 = func(decorator(func=sample_func3))


@decorator_func_with_params
def sample_func4(param):
    print(param)


if __name__ == '__main__':
    # print('--- 1 ---')
    # sample_func1()

    # print('\n--- 2 ---')
    # sample_func2()

    # print('\n--- 3 ---')
    # sample_func3()

    print('\n--- 4 ---')
    sample_func4('My hello world')
