from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    age: int


USERS = [
    User(id=1, name='Patryk', age=25),
    User(id=2, name='Olaf', age=15),
]


def validate_user(user, user_id):
    if user.id == user_id:
        if user.age < 18:
            return False
    return True


def only_for_adults_decorator(func):
    def wrapper(*args, **kwargs):

        user_id = kwargs.get('user_id')
        if user_id:

            for user in USERS:
                if not validate_user(user=user, user_id=user_id):
                    return 'Failed! You are not adult!'

        return func(*args, **kwargs)

    return wrapper


@only_for_adults_decorator
def get_content(user_id: int):
    return 'Success! Content only for adults.'


if __name__ == '__main__':
    result = get_content(user_id=1)
    print(result)