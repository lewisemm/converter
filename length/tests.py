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

    def test_centimetre_to_inch_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "inch",
            "input_value": round(123.442, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 48.599)

    def test_centimetre_to_kilometre_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "kilometre",
            "input_value": round(439723.442664, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 4.397)

    def test_centimetre_to_yard_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "yard",
            "input_value": round(568.2326599, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 6.214)

    def test_centimetre_to_millimetre_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "millimetre",
            "input_value": round(45.455, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 454.55)

    def test_centimetre_to_foot_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "foot",
            "input_value": round(346.653, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 11.373)

    def test_metre_to_centimetres_conversion(self):
        data = {
            "input_unit": "metre",
            "output_unit": "centimetre",
            "input_value": round(12.264, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 1226.4)

    def test_metre_to_miles_conversion(self):
        data = {
            "input_unit": "metre",
            "output_unit": "mile",
            "input_value": round(3486.25479998, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 2.166)

    def test_metre_to_inch_conversion(self):
        data = {
            "input_unit": "metre",
            "output_unit": "inch",
            "input_value": round(23.3698, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 920.070)

    def test_metre_to_kilometre_conversion(self):
        data = {
            "input_unit": "metre",
            "output_unit": "kilometre",
            "input_value": round(85.369, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.085)

    def test_metre_to_yard_conversion(self):
        data = {
            "input_unit": "metre",
            "output_unit": "yard",
            "input_value": round(54.5874, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 59.697)

    def test_metre_to_millimetre_conversion(self):
        data = {
            "input_unit": "metre",
            "output_unit": "millimetre",
            "input_value": round(9, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 9000)

    def test_metre_to_foot_conversion(self):
        data = {
            "input_unit": "metre",
            "output_unit": "foot",
            "input_value": round(5874.25, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 19272)

    def test_mile_to_centimetre_conversion(self):
        data = {
            "input_unit": "mile",
            "output_unit": "centimetre",
            "input_value": round(12.563, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 2021813.842)

    def test_mile_to_metres_conversion(self):
        data = {
            "input_unit": "mile",
            "output_unit": "metre",
            "input_value": round(24.254, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 39032.932)

    def test_mile_to_inch_conversion(self):
        data = {
            "input_unit": "mile",
            "output_unit": "inch",
            "input_value": round(45.789, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 2901183.829)

    def test_mile_to_kilometre_conversion(self):
        data = {
            "input_unit": "mile",
            "output_unit": "kilometre",
            "input_value": round(15.897, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 25.584)

    def test_mile_to_yard_conversion(self):
        data = {
            "input_unit": "mile",
            "output_unit": "yard",
            "input_value": round(78.123, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 137496.138)

    def test_mile_to_millimetre_conversion(self):
        data = {
            "input_unit": "mile",
            "output_unit": "millimetre",
            "input_value": round(568.214, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 914449518.76)

    def test_mile_to_foot_conversion(self):
        data = {
            "input_unit": "mile",
            "output_unit": "foot",
            "input_value": round(48.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 254732.967)

    def test_inch_to_centimetre_conversion(self):
        data = {
            "input_unit": "inch",
            "output_unit": "centimetre",
            "input_value": round(48.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 122.542)

    def test_inch_to_metre_conversion(self):
        data = {
            "input_unit": "inch",
            "output_unit": "metre",
            "input_value": round(48.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 1.225)

    def test_inch_to_mile_conversion(self):
        data = {
            "input_unit": "inch",
            "output_unit": "mile",
            "input_value": round(48.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.001)

    def test_inch_to_yard_conversion(self):
        data = {
            "input_unit": "inch",
            "output_unit": "yard",
            "input_value": round(48.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 1.34)

    def test_inch_to_millimetre_conversion(self):
        data = {
            "input_unit": "inch",
            "output_unit": "millimetre",
            "input_value": round(48.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 1225.423)

    def test_inch_to_foot_conversion(self):
        data = {
            "input_unit": "inch",
            "output_unit": "foot",
            "input_value": round(48.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 4.02)

    def test_kilometre_to_centimtre_conversion(self):
        data = {
            "input_unit": "kilometre",
            "output_unit": "centimetre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 48424500.0)

    def test_kilometre_to_metre_conversion(self):
        data = {
            "input_unit": "kilometre",
            "output_unit": "metre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 484245.0)

    def test_kilometre_to_mile_conversion(self):
        data = {
            "input_unit": "kilometre",
            "output_unit": "mile",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 300.896)

    def test_kilometre_to_inch_conversion(self):
        data = {
            "input_unit": "kilometre",
            "output_unit": "inch",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 19064763.779)

    def test_kilometre_to_yard_conversion(self):
        data = {
            "input_unit": "kilometre",
            "output_unit": "yard",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 529576.772)

    def test_kilometre_to_millimetre_conversion(self):
        data = {
            "input_unit": "kilometre",
            "output_unit": "millimetre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 484245000.0)

    def test_kilometre_to_foot_conversion(self):
        data = {
            "input_unit": "kilometre",
            "output_unit": "foot",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 1588730.315)

    def test_yard_to_centimetre_conversion(self):
        data = {
            "input_unit": "yard",
            "output_unit": "centimetre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 44279.363)

    def test_yard_to_metre_conversion(self):
        data = {
            "input_unit": "yard",
            "output_unit": "metre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 442.794)

    def test_yard_to_mile_conversion(self):
        data = {
            "input_unit": "yard",
            "output_unit": "mile",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.275)

    def test_yard_to_inch_conversion(self):
        data = {
            "input_unit": "yard",
            "output_unit": "inch",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 17432.82)

    def test_yard_to_kilometre_conversion(self):
        data = {
            "input_unit": "yard",
            "output_unit": "kilometre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.443)

    def test_yard_to_millimetre_conversion(self):
        data = {
            "input_unit": "yard",
            "output_unit": "millimetre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 442793.628)

    def test_yard_to_foot_conversion(self):
        data = {
            "input_unit": "yard",
            "output_unit": "foot",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 1452.735)

    def test_millimetre_to_centimetre_conversion(self):
        data = {
            "input_unit": "millimetre",
            "output_unit": "centimetre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 48.425)

    def test_millimetre_to_metre_conversion(self):
        data = {
            "input_unit": "millimetre",
            "output_unit": "metre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.484)

    def test_millimetre_to_mile_conversion(self):
        data = {
            "input_unit": "millimetre",
            "output_unit": "mile",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.0)

    def test_millimetre_to_inch_conversion(self):
        data = {
            "input_unit": "millimetre",
            "output_unit": "inch",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 19.065)

    def test_millimetre_to_kilometre_conversion(self):
        data = {
            "input_unit": "millimetre",
            "output_unit": "kilometre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.0)

    def test_millimetre_to_yard_conversion(self):
        data = {
            "input_unit": "millimetre",
            "output_unit": "yard",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.53)

    def test_millimetre_to_foot_conversion(self):
        data = {
            "input_unit": "millimetre",
            "output_unit": "foot",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 1.589)

    def test_foot_to_centimetre_conversion(self):
        data = {
            "input_unit": "foot",
            "output_unit": "centimetre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 14759.788)

    def test_foot_to_metre_conversion(self):
        data = {
            "input_unit": "foot",
            "output_unit": "metre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 147.598)

    def test_foot_to_mile_conversion(self):
        data = {
            "input_unit": "foot",
            "output_unit": "mile",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.092)

    def test_foot_to_inch_conversion(self):
        data = {
            "input_unit": "foot",
            "output_unit": "inch",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 5810.94)

    def test_foot_to_kilometre_conversion(self):
        data = {
            "input_unit": "foot",
            "output_unit": "kilometre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 0.148)

    def test_foot_to_yard_conversion(self):
        data = {
            "input_unit": "foot",
            "output_unit": "yard",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 161.415)

    def test_foot_to_millimetre_conversion(self):
        data = {
            "input_unit": "foot",
            "output_unit": "millimetre",
            "input_value": round(484.245, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 147597.876)

