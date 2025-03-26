from django.test import TestCase
from product.models import Category
from product.factories import CategoryFactory

class CategoryFactoryTest(TestCase):
    def test_category_creation(self):
        category = CategoryFactory.create()
        self.assertIsInstance(category, Category)
        self.assertTrue(category.title)
        self.assertTrue(category.slug)
        self.assertTrue(category.description)
        self.assertTrue(category.active)
