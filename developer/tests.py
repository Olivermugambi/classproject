from django.test import TestCase
from developer.models import *
from django.utils import timezone

class DeveloperTestCase(TestCase):
    def setUp(self):
        Developer.objects.create(developer_name="Rick Lotodo", email="admin@company.co.ke",telephone="+123456789", registration_date=timezone.now())
        Developer.objects.create(developer_name="Derric Oloo.", email="admin@kenya.org", telephone="+45326722211", registration_date=timezone.now())
        Developer.objects.create(developer_name="Oliver Kumu", email="developer@idea.com", telephone="+252373898322", registration_date=timezone.now())
                
    def test_developer_emails_are_unique(self):
        """Non-unique emails are iodentified"""
        rick = Developer.objects.get(developer_name="Rick Lotodo")
        derric = Developer.objects.get(developer_name="Derric Oloo.")
        kumu = Developer.objects.get(developer_name="Oliver Kumu")
        self.assertNotEqual(rick.email, derric.email)
        self.assertNotEqual(derric.email, kumu.email)
        self.assertNotEqual(kumu.email, rick.email)

    def test_developer_telephones_are_unique(self):
        """Non-unique telephone numbers are iodentified"""
        rick = Developer.objects.get(developer_name="Rick Lotodo")
        derric = Developer.objects.get(developer_name="Derric Oloo.")
        kumu = Developer.objects.get(developer_name="Oliver Kumu")
        self.assertNotEqual(rick.telephone, derric.telephone)
        self.assertNotEqual(derric.telephone, kumu.telephone)
        self.assertNotEqual(kumu.telephone, rick.telephone)

    def test_developer_names_are_not_unique(self):
        """Unique telephone numbers are iodentified"""
        rick = Developer.objects.get(developer_name="Rick Lotodo")
        derric = Developer.objects.get(developer_name="Derric Oloo.")
        kumu = Developer.objects.get(developer_name="Oliver Kumu")
        self.assertNotEqual(rick.developer_name, derric.developer_name)
        self.assertNotEqual(derric.developer_name, kumu.developer_name)
        self.assertNotEqual(kumu.developer_name, rick.developer_name)