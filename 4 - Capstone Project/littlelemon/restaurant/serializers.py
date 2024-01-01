"""
serializers.py

"""


from rest_framework import serializers
from .models import Booking, Menu


class BookingSerializer(serializers.ModelSerializer):
    """Booking Table Serializer"""

    class Meta:
        """metadata"""

        model = Booking
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    """Menu Table Serializer"""

    class Meta:
        """metadata"""

        model = Menu
        fields = "__all__"
