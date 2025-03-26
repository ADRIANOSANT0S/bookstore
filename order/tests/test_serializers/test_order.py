import pytest

from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory


@pytest.mark.django_db
def test_order_creation():
    user = UserFactory()
    product1 = ProductFactory()
    product2 = ProductFactory()

    order = OrderFactory(user=user, product=[product1, product2])

    assert order.user == user
    assert order.product.count() == 2
