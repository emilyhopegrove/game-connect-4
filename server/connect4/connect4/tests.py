from django.test import TestCase
from django.urls import reverse

class SimpleTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'About Us')

