from django.test import TestCase, Client
from django.urls import reverse


class TestLengthConversion(TestCase):
    """
    This class contains tests that convert measurements from one
    unit of measurement to another.
    """

    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.client = Client()
        self.url = reverse("length:convert")

    def test_centimetre_to_metre_conversion(self):
        """
        Tests conversion of centimetre measurements to metre.
        """
        data = {
            "input_unit": "centimetre",
            "output_unit": "metre",
            "input_value": round(8096.894, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 80.969)

    def test_centimetre_to_mile_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "mile",
            "input_value": round(985805791.3527409, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 6125.511)