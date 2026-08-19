import pytest
from cart import Cart

@pytest.fixture(scope="function") # 기본값

def cart():
    print("\n [준비] 새 장바구니")
    c = Cart()
    yield c
    print(" [정리] 장바구니 비움")
    c.items.clear()

@pytest.mark.parametrize("price, qty, expected", [
    (12000, 2, 24000),
    (0, 5, 0),
    (1000, 1, 1000),
])

def test_total(cart, price, qty, expected):
    cart.add("item", price, qty)
    assert cart.total() == expected

