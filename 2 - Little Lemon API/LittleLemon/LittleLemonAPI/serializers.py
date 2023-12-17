"""
serializers.py

"""


from rest_framework import serializers
from django.contrib.auth.models import User

from . import models


class UserSerializer(serializers.ModelSerializer):
    """Serializer for 'User'"""

    class Meta:
        """Serializer metadata"""

        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        """Ensure created password is hashed"""
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        instance.is_active = True
        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class SingleUserSerializer(serializers.ModelSerializer):
    """Serializer for endpoint 'users/me'"""

    class Meta:
        """Serializer metadata"""

        model = User
        fields = ["id", "username", "email", "password"]


class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer class for the 'MenuItem' model"""

    category = serializers.PrimaryKeyRelatedField(
        queryset=models.Category.objects.all()
    )

    class Meta:
        """Serializer metadata"""

        model = models.MenuItem
        fields = ["id", "category", "title", "price", "featured"]


class CategorySerializer(serializers.ModelSerializer):
    """Serializer class for the 'Category' model"""

    class Meta:
        """Serializer metadate"""

        model = models.Category
        fields = ["id", "slug", "title"]


class CartSerializer(serializers.ModelSerializer):
    """Serializer class for the 'Cart' model"""

    class Meta:
        """Serializer metadata"""

        model = models.Cart
        fields = ["user", "menu_item", "quantity", "unit_price", "price"]


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer class for the 'OrderItem' model"""

    class Meta:
        """Serializer metadata"""

        model = models.OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """Serializer class for the 'Order' model"""

    order_item = OrderItemSerializer(many=True, read_only=True, source="order")

    class Meta:
        """Serializer metadata"""

        model = models.Order
        fields = [
            "id",
            "user",
            "order_item",
            "delivery_crew",
            "delivery_status",
            "total_price",
            "date",
        ]


class GroupSerializer(serializers.Serializer):
    """Facilitates input of a username to add to a group"""

    username = serializers.CharField()
