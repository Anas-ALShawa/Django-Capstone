

# Create your tests here.
from django.test import TestCase
from restaurant.models import Menu
from django.test import TestCase


class MenuTest(TestCase):
    def setUp(self):
        # Create initial test data
        self.obj = Menu.objects.create(
            Title='pizza',
            Price=12.5,
            Inventory = 100,
        )

    def test_model_str(self):
        self.assertEqual(str(self.obj), 'pizza')

    def test_model_field_value(self):
        self.assertEqual(self.obj.Title, 'pizza')
        self.assertEqual(self.obj.Price, 12.5)
        self.assertEqual(self.obj.Inventory, 100)
