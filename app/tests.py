from django.test import TestCase
from .models import VaccineList
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.vaccinelist_data = {'name': 'Hep B'}
        self.response = self.client.post(
            reverse('create'),
            self.vaccinelist_data,
            format="json")

    def test_api_can_create_a_vaccinelist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class ModelTestCase(TestCase):
    """This class defines the test suite for the vaccinelist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.vaccinelist_name = "Vaccine List"
        self.vaccinelist = VaccineList(name=self.vaccinelist_name)

    def test_model_can_create_a_vaccinelist(self):
        """Test the vaccinelist model can create a bucketlist."""
        old_count = VaccineList.objects.count()
        self.vaccinelist.save()
        new_count = VaccineList.objects.count()
        self.assertNotEqual(old_count, new_count)
