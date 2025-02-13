import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory
from product.models import Product
from order.models import Order


class TestOrderViewsSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='cars')
        self.product = ProductFactory(title='Porsche', price=700000, category=[self.category])
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        response = self.client.get(
            reverse('order-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)[0]
        self.assertEqual(order_data['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['product'][0]['price'], self.product.price)
        self.assertEqual(order_data['product'][0]['active'], self.product.active)
        self.assertEqual(order_data['product'][0]['category'][0]['title'], self.category.title) 

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory() 
        data = json.dumps({
            'product_id': [product.id],
            'user': user.id
        })

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
        print('response ', response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        create_order = Order.objects.get(user=user)
        

