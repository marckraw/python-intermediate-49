"""
PRODUCTS

Napisz trzy funkcje korzystajace z lambda realizujace nastepujace zadania:
* filter - zwraca tylko produkty znajdujace sie w koszyku (in_cart == True)
* reduce - zwraca sume kosztów produktów w liście
* map - zwraca ceny produktów po obniżce o 50%

"""
from dataclasses import dataclass
from functools import reduce
from typing import Callable


@dataclass
class Product:
    id: int
    name: str
    cost: float
    in_cart: bool


PRODUCT_LIST = [
    Product(id=23, name='Monitor', cost=700, in_cart=True),
    Product(id=126, name='Glasses', cost=600, in_cart=False),
    Product(id=16, name='Mouse', cost=100, in_cart=True),
    Product(id=17, name='Keyboard', cost=150, in_cart=True),
    Product(id=65, name='Book', cost=60, in_cart=False),
    Product(id=23, name='Desk lamp', cost=40, in_cart=False),
]

EXPECTED_PRODUCT_LIST = [
    Product(id=23, name='Monitor', cost=700, in_cart=True),
    Product(id=16, name='Mouse', cost=100, in_cart=True),
    Product(id=17, name='Keyboard', cost=150, in_cart=True),
]
EXPECTED_TOTAL_COST = 950
DISCOUNTED_PRICES = [350, 50, 75]


def is_in_cart(product: Product) -> bool:
    return product.in_cart


def make_discount(product: Product):
    return product.cost * 0.5


def make_discount_extended(discount: float) -> Callable:
    def internal_make_discount(product: Product):
        return product.cost * discount

    return internal_make_discount


def make_discount_extended(discount: float) -> Callable:
    return lambda item: item.cost * discount


func = make_discount_extended(discount=0.25)
print(PRODUCT_LIST[0])
print(func(product=PRODUCT_LIST[0]))


def add_price(acc: float, product: Product):
    return acc + product.cost


if __name__ == '__main__':
    cart = list(filter(lambda item: item.in_cart, PRODUCT_LIST))
    cart = list(filter(is_in_cart, PRODUCT_LIST))
    cart = [item for item in PRODUCT_LIST if item.in_cart]
    assert cart == EXPECTED_PRODUCT_LIST

    total_cost = reduce(
        lambda total, item: total + item.cost,
        cart,
        0.0,
    )
    total_cost = reduce(add_price, cart, 0.0)
    # to nie jest equivalent!
    # jezeli zamiast dodawania mielibyśmy np. -, to zauważmy, że już by to nie działało
    # Python nie posiada equivalentu reduce
    total_cost = sum([item.cost for item in cart])
    assert total_cost == EXPECTED_TOTAL_COST

    discounted_prices = list(map(lambda item: item.cost * 0.5, cart))
    discounted_prices = list(map(make_discount, cart))
    discounted_prices = list(map(make_discount_extended(discount=0.25), cart))
    discounted_prices = [item.cost * 0.5 for item in cart]
    assert discounted_prices == DISCOUNTED_PRICES
