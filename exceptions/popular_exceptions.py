POPULAR_EXCEPTIONS = [
    AssertionError,
    AttributeError,
    IOError,
    IndexError,
    ImportError,
    KeyError,
    NameError,
    ValueError,
    ZeroDivisionError,
    SyntaxError,
]


def throw_assertion_error():
    # assert False
    assert 1 == 0


def throw_attribute_error():
    var = 1
    var.append(2)


def throw_io_error():
    file = open('not-existing-file.txt')


def throw_index_error():
    sample_list = [1, 2, 3]
    print(sample_list[3])


def throw_import_error():
    import ala_ma_kota


def throw_key_error():
    sample_dict = {
        'test1': 1,
        'test2': 2,
    }
    print(sample_dict['test3'])


# def throw_name_error():
#     prin('Our beautiful string!')


def throw_value_error():
    int('sample_string')


def throw_zero_division_error():
    print(1 / 0)


# def throw_syntax_error():
#     if True
#         print('If with :')


if __name__ == '__main__':
    throw_assertion_error()
    throw_attribute_error()
    throw_io_error()
    throw_index_error()
    throw_import_error()
    throw_key_error()
    # throw_name_error()
    throw_value_error()
    throw_zero_division_error()
    # throw_syntax_error()
