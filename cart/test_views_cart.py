from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart


class TestCartViews(SimpleTestCase):

    def test_view_cart_resolves(self):
        url = reverse('view_cart')
        self.assertEqual(resolve(url).func, view_cart)

    def test_add_to_cart_resolves(self):
        url = reverse('add_to_cart', args=['item_id'])
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_adjust_cart_resolves(self):
        url = reverse('adjust_cart', args=['item_id'])
        self.assertEqual(resolve(url). func, adjust_cart)

    def test_remove_from_cart_resolves(self):
        url = reverse('remove_from_cart', args=['item_id'])
        self.assertEqual(resolve(url).func, remove_from_cart)
