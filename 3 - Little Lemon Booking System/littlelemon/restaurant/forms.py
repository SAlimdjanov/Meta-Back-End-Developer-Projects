"""
forms.py

"""


from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    """Booking Form Model"""

    class Meta:
        """Model metadata"""

        model = Booking
        fields = "__all__"
