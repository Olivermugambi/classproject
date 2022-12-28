from django.test import TestCase
from customermanagement.models import *
from django.utils import timezone

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer_Profile.objects.create(customer_name="Atlas Ltd.", customer_email="admin@admin.co.ke", customer_telephone="+254765432", created_on=timezone.now())
        Customer_Profile.objects.create(customer_name="Dennis Oloo.", customer_email="admin@admin.com", customer_telephone="+25476234532", created_on=timezone.now())
        Customer_Profile.objects.create(customer_name="123456", customer_email="general@email.com", customer_telephone="+252373898322", created_on=timezone.now())
                
    def test_customer_emails_are_unique(self):
        """Non-unique emails are iodentified"""
        atlas = Customer_Profile.objects.get(customer_name="Atlas Ltd.")
        dennis = Customer_Profile.objects.get(customer_name="Dennis Oloo.")
        other = Customer_Profile.objects.get(customer_name="123456")
        self.assertNotEqual(atlas.customer_email, dennis.customer_email)
        self.assertNotEqual(other.customer_email, dennis.customer_email)
        self.assertNotEqual(other.customer_email, atlas.customer_email)

    def test_customer_telephones_are_unique(self):
        """Non-unique telephone numbers are iodentified"""
        atlas = Customer_Profile.objects.get(customer_name="Atlas Ltd.")
        dennis = Customer_Profile.objects.get(customer_name="Dennis Oloo.")
        other = Customer_Profile.objects.get(customer_name="123456")
        self.assertNotEqual(atlas.customer_telephone, dennis.customer_telephone)
        self.assertNotEqual(other.customer_telephone, dennis.customer_telephone)
        self.assertNotEqual(other.customer_telephone, atlas.customer_telephone)