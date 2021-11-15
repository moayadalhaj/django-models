from django.http import response
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SnacksTests(TestCase):

    def test_snack_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_page_tepmlate(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')