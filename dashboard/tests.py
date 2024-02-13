from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Items, Category
from .serializers import ItemSerializer, CategorySerializer


class ItemSerializerTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(category_name='Electronics')
        self.item = Items.objects.create(
            sku_code='SKU1234',
            item_name='Smartphone',
            category_id=self.category,
            cost=999.99
        )

    def test_item_serializer(self):
        serializer = ItemSerializer(instance=self.item)
        data = serializer.data
        self.assertEqual(data['sku_code'], 'SKU1234')
        self.assertEqual(data['item_name'], 'Smartphone')
        self.assertEqual(data['cost'],  999.99)
        self.assertIsInstance(data['category_id'], dict)
        self.assertEqual(data['category_id']['category_name'], 'Electronics')

    def test_item_serializer_create(self):
        valid_payload = {
            'sku_code': 'SKU5678',
            'item_name': 'Tablet',
            'category_id': {'category_name': 'Electronics'},
            'cost':  499.99
        }
        response = self.client.post(reverse('api/items/'), data=valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Items.objects.count(),  2)
        self.assertEqual(Items.objects.get(sku_code='SKU5678').item_name, 'Tablet')

