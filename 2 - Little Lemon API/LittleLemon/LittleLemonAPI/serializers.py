"""
serializers.py

"""


from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    """Serializer for 'User'"""

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        """Serializer metadata"""

        model = User
        fields = ["user", "username", "email", "password"]


class CategorySerializer(serializers.ModelSerializer):
    """Serializer class for the 'Category' model"""

    class Meta:
        """Serializer metadata"""

        model = models.Category
        fields = ["slug", "title"]


class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer class for the 'MenuItem' model"""

    class Meta:
        """Serializer metadata"""

        model = models.MenuItem
        fields = ["title", "price", "featured", "category"]


class CartSerializer(serializers.ModelSerializer):
    """Serializer class for the 'Cart' model"""

    class Meta:
        """Serializer metadata"""

        model = models.Cart
        fields = ["user", "menu_item", "quantity", "unit_price", "price"]


class OrderSerializer(serializers.ModelSerializer):
    """Serializer class for the 'Order' model"""

    class Meta:
        """Serializer metadata"""

        model = models.Order
        fields = ["user", "delivery_crew", "delivery_status", "total_price", "date"]


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer class for the 'Cart' model"""

    class Meta:
        """Serializer metadata"""

        model = models.OrderItem
        fields = ["order", "menu_item", "quantity", "unit_price", "price"]
