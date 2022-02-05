"""
USER HAS PERMISSION

Naszym zadaniem jest napisanie dekoratora sprawdzającego czy dany uzytkownik ma dostęp do wykonania
danej operacji. W tym przypadku mowimy tutaj o dostepie do usuniecia post'a z platformy typu
Facebook. Usunąć post może tylko autor postu lub administrator strony. Zwykły użytkownik, który
tylko czyta ten post nie może tego zrobić.

W słowniku USERS mamy zdefiniowanych trzech użytkowników o różnych poziomach dostępów.

Nasz dekorator powinien przyjmowac jako parametry liste zawierającą poziomy dostępów z jakimi
użytkownik może wykonać udekorowaną funkcję. Przykładowe wywołanie jest zareprezentowane na
definicji funkcji delete_post.
* dekorator wykonuje funkcje w momencie gdy uzytkownik, który wykonał operacje ma do niej dostęp
* w przeciwnym wypadku dekorator zwraca False

Napisano już testy mające na celu sprawdzenie poprawnego działania udekorowanej funkcji
"""


class PermissionModel:
    READER = 0
    OWNER = 1
    ADMIN = 2


USERS = [
    {
        "id": 1,
        "name": "Yvette Kelley",
        "sex": "F",
        "age": "32",
        "permission_level": PermissionModel.ADMIN,
    },
    {
        "id": 2,
        "name": "Isabel Byrne",
        "sex": "F",
        "age": "65",
        "permission_level": PermissionModel.OWNER,
    },
    {
        "id": 3,
        "name": "Kyran Mcarthur",
        "sex": "M",
        "age": "26",
        "permission_level": PermissionModel.READER,
    },
]


def check_permission(permission_list):
    pass


@check_permission([PermissionModel.OWNER, PermissionModel.ADMIN])
def delete_post(user, post_id):
    return f"User with id {user['id']} deleted post {post_id}"


if __name__ == '__main__':
    assert delete_post(USERS[0], 1) == "User with id 1 deleted post 1"
    assert delete_post(USERS[1], 2) == "User with id 2 deleted post 2"
    assert delete_post(USERS[2], 3) is False
