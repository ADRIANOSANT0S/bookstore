import json

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)
        token.save()

        self.product = ProductFactory(
            title='Pro Controller',
            price=50000
        )
    
    def test_get_all_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # import pdb; pdb.set_trace()    

        product_data = json.loads(response.content)
        self.assertEqual(product_data['results'][0]['title'], self.product.title)
        self.assertEqual(product_data['results'][0]['price'], self.product.price)
        self.assertEqual(product_data['results'][0]['active'], self.product.active)

    def test_create_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        category = CategoryFactory()
        data = json.dumps({
            'title': 'Porsche',
            'price': 700000,
            'category_id': [category.id]
        })

        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1' }),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        create_product = Product.objects.get(title='Porsche')

        self.assertEqual(create_product.title, 'Porsche')
        self.assertEqual(create_product.price, 700000)


