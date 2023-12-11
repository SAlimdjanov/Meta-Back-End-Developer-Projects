"""
view.py

Views for required API endpoints

"""

from rest_framework import generics
from django.contrib.auth.models import User
from . import models
from . import serializers


class UserView(generics.ListCreateAPIView):
    """View class for model 'User'"""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class CategoryView(generics.ListCreateAPIView):
    """View class for model 'Category'"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class MenuItemView(generics.ListCreateAPIView):
    """View class for model 'MenuItem'"""

    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


class SingleMenuItemView(generics.RetrieveAPIView):
    """Single menu item view"""

    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


class CartView(generics.ListCreateAPIView):
    """View class for model 'Cart'"""

    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer


class OrderView(generics.ListCreateAPIView):
    """View class for model 'Order'"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderItemView(generics.RetrieveAPIView):
    """View class for model 'OrderItem'"""

    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
