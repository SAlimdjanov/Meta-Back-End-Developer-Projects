"""
urls.py

URL configuration at the API level

"""


from django.urls import path

from . import views


urlpatterns = [
    path("users", views.CreateUserView.as_view()),
    path("menu-items", views.MenuItemView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("categories", views.CategoryView.as_view()),
    path(
        "groups/managers/users",
        views.ManagerGroupView.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
    path(
        "groups/delivery-crew/users",
        views.DeliveryCrewView.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
    path("cart/menu-items", views.CartView.as_view()),
    path("orders", views.OrderView.as_view()),
    path("orders/<int:pk>", views.OrderView.as_view()),
]
