from django.test import TestCase, Client
from django.urls import reverse

class TestStorageConversion(TestCase):
    """
    This class contains tests that convert measurements from one
    unit of measurement to another.
    """
    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.client = Client()
        self.url = reverse("storage:convert")

    def test_mb_to_gb_conversion(self):
        """
        Tests conversion of megabytes  to gigabytes.
        """
        data = {
            "input_unit": "mb",
            "output_unit": "gb",
            "input_value": round(784.568, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.766)

    def test_mb_to_tb_conversion(self):
        data = {
            "input_unit": "mb",
            "output_unit": "tb",
            "input_value": round(97784.568, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.093)

    def test_gb_to_mb_conversion(self):
        data = {
            "input_unit": "gb",
            "output_unit": "mb",
            "input_value": round(784.568, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 803397.632)

    def test_gb_to_tb_conversion(self):
        data = {
            "input_unit": "gb",
            "output_unit": "tb",
            "input_value": round(784.568, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.766)

    def test_tb_to_gb_conversion(self):
        data = {
            "input_unit": "tb",
            "output_unit": "gb",
            "input_value": round(784.568, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 803397.632)

    def test_tb_to_mb_conversion(self):
        data = {
            "input_unit": "tb",
            "output_unit": "mb",
            "input_value": round(784.568, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 822679175.168)