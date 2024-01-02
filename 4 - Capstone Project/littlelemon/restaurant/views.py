"""
views.py

"""


from django.shortcuts import render

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


def home(request):
    """Renders home page template

    Args:
        (django.http.HttpRequest): Request object

    Returns:
        django.http.HttpResponse: HTTP response object with loaded template
    """
    return render(request, "index.html", {})


class MenuItemView(ListCreateAPIView):
    """View menu items"""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    """View a item"""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(ModelViewSet):
    """View bookings"""

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
