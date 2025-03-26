from django.test import TestCase
from product.models import Product
from product.factories import ProductFactory


class ProductFactoryTest(TestCase):
    def test_product_create(self):
        product = ProductFactory.create()
        self.assertIsInstance(product, Product)
        self.assertTrue(product.title)
        self.assertTrue(product.price > 0)
        self.assertIsNotNone(product.category)
