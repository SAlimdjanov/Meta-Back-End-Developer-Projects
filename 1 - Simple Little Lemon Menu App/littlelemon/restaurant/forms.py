"""
forms.py

"""

from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    """Loads form data on the booking page

    Args:
        ModelForm (django.forms): Template class to create HTML forms from django models
    """
    class Meta:
        """Meta Class"""
        model = Booking
        fields = "__all__"
