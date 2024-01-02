"""
test_models.py

"""


from django.test import TestCase
from ..models import Booking, Menu


class BookingTest(TestCase):
    """Test booking model"""

    def test_get_item(self):
        """Test create item"""
        item = Menu.objects.create(title="TestItem", price=79.99, inventory=50)
        self.assertEqual(str(item), "TestItem : 79.99")


class MenuTest(TestCase):
    """Test menu model"""

    def test_get_item(self):
        """Test create item"""
        item = Booking.objects.create(
            name="John Doe", no_of_guests=3, booking_date="2024-01-13T15:00:00Z"
        )
        self.assertEqual(
            str(item), "name: John Doe - guests: 3 - date: 2024-01-13T15:00:00Z"
        )
