  
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import email_collect


class TestNewsletterViews(SimpleTestCase):

    def test_email_collect_resolves(self):
        url = reverse('email_collect')
        self.assertEqual(resolve(url).func, email_collect)
