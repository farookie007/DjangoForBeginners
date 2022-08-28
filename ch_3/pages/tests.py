from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class HomeTests(SimpleTestCase):
    def test_url_exists_at_current_location(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class AboutTests(SimpleTestCase):
    def test_url_exists_at_current_location(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
