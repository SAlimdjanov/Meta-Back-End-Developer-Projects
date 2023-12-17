"""
view.py

Views for required API endpoints

"""


from copy import deepcopy

from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

from . import serializers
from . import models


class CreateUserView(generics.CreateAPIView):
    """Create a new user"""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class MenuItemView(generics.ListCreateAPIView):
    """View menu items"""

    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    ordering_fields = ["price"]
    search_fields = ["category__title"]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Obtain permissions when a request is made"""
        permission_classes = []

        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveAPIView):
    """View a single menu item"""

    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Obtain permissions when a request is made"""
        permission_classes = []

        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class CategoryView(generics.ListCreateAPIView):
    """View menu categories"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Obtain permissions when a request is made"""
        permission_classes = []

        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class CartView(generics.ListCreateAPIView):
    """View and add to current Cart"""

    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        """View only the cart assigned to the current user"""
        return models.Cart.objects.all().filter(user=self.request.user)

    def delete(self, request):
        """Delete the Cart"""
        models.Cart.objects.all().filter(user=self.request.user).delete()
        return Response({"message": "Cart deleted successfully"}, status.HTTP_200_OK)


class OrderView(generics.ListCreateAPIView):
    """View Order Information"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_total_price(self, current_user):
        """Returns the total price of a cart assigned to a particular user"""
        total_price = 0
        cart_items = models.Cart.objects.all().filter(user=current_user).all()

        for item in cart_items.values():
            total_price += item["price"]

        return total_price

    def get_queryset(self):
        """View order information depending on the current user's assigned group"""

        # If no group is assigned (Customers)
        if self.request.user.groups.count() == 0:
            return models.Order.objects.all().filter(user=self.request.user)

        # Show orders only assigned to the delivery crew member logged in
        if self.request.user.groups.filter(name="Delivery Crew").exists:
            return models.Order.objects.all().filter(delivery_crew=self.request.user)

        # If not a customer or delivery crew member (hence manager or admin), return all info
        return models.Order.objects.all()

    def create(self, request, *args, **kwargs):
        """Create (POST) an order"""

        # Check number of menu items in cart before proceeding to create an order
        menu_item_count = (
            models.Cart.objects.all().filter(user=self.request.user).count()
        )

        if menu_item_count == 0:
            return Response(
                {"message": "Error: No Items Present in the Cart"},
                status.HTTP_400_BAD_REQUEST,
            )

        request_data = deepcopy(request.data)
        total_price = self.get_total_price(self.request.user)
        request_data["total_price"] = total_price
        request_data["current_user"] = self.request.user.id
        serializer = serializers.OrderSerializer(data=request_data)

        # If serialized data is valid
        if serializer.is_valid():
            current_order = serializer.save()
            order_items = models.Cart.objects.all().filter(user=self.request.user).all()

            # Save all the order items
            for item in order_items.values():
                order_item = models.OrderItem(
                    order=current_order,
                    menu_item_id=item["menu_item_id"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
                order_item.save()

            # Delete the cart once done
            models.Cart.objects.all().filter(user=self.request.user).delete()

            result = deepcopy(serializer.data)
            result["total_price"] = total_price

            return Response(serializer.data, status.HTTP_200_OK)


class SingleOrderView(generics.RetrieveUpdateAPIView):
    """View and/or change Order details"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def update(self, request, *args, **kwargs):
        """Update order details"""

        # If customer, do not permit
        if self.request.user.groups.count() == 0:
            return Response({"message": "Error: Forbidden"}, status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)


class ManagerGroupView(viewsets.ViewSet):
    "View and modify the Manager group"

    permission_classes = [IsAdminUser]
    serializer_class = serializers.GroupSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def list(self, request):
        """Display managers"""
        users = User.objects.all().filter(groups__name="Managers")
        items = serializers.UserSerializer(users, many=True)

        return Response(items.data)

    @action(detail=False, methods=["post"])
    def create(self, request):
        """Add user to the manager group"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Managers")
        managers.user_set.add(user)

        return Response(
            {"message": f"Success: User {user} added to the manager group"},
            status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["delete"])
    def destroy(self, request):
        """Remove a user from the manager group"""
        user = get_object_or_404(User, username=request.data["username"])
        managers = Group.objects.get(name="Manager")
        managers.user_set.remove(user)

        return Response(
            {"message": f"Success: User {user} removed from the manager group"},
            status.HTTP_200_OK,
        )


class DeliveryCrewView(viewsets.ViewSet):
    """View and modify the Delivery Crew group"""

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GroupSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def list(self, request):
        """View the delivery crew"""
        users = User.objects.all().filter(groups__name="Delivery Crew")
        items = serializers.UserSerializer(users, many=True)

        return Response(items.data, status.HTTP_200_OK)

    def create(self, request):
        """Add a member to the delivery crew"""

        # If admin or manager only
        if self.request.user.is_superuser is False:
            if self.request.user.groups.filter(name="Manager").exists() is False:
                return Response(
                    {"message": "Error: Forbidden operation"}, status.HTTP_403_FORBIDDEN
                )

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        user = get_object_or_404(User, username=username)
        delivery_crew = Group.objects.get(name="Delivery Crew")
        delivery_crew.user_set.add(user)

        return Response(
            {"message": f"Success: User {user} added to the delivery crew group"},
            status.HTTP_201_CREATED,
        )

    def destroy(self, request):
        """Remove a user from the delivery crew"""

        # Only allowed if superuser or manager
        if self.request.user.is_superuser is False:
            if self.request.user.groups.filter(name="Manager").exists() is False:
                return Response({"message": "forbidden"}, status.HTTP_403_FORBIDDEN)

        user = get_object_or_404(User, username=request.data["username"])
        delivery_crew = Group.objects.get(name="Delivery Crew")
        delivery_crew.user_set.remove(user)

        return Response(
            {"message": f"Success: User {user} removed from the delivery crew group"},
            status.HTTP_200_OK,
        )
