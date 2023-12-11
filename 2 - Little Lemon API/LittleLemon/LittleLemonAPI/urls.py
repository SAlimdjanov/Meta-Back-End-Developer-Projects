"""
urls.py

URL configuration at the API level

"""


from django.urls import path
from . import views


urlpatterns = [
    path("users", views.UserView.as_view()),
    path("menu-items", views.MenuItemView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("category", views.CategoryView.as_view()),
    path("cart", views.CartView.as_view()),
    path("order", views.OrderView.as_view()),
    path("order-items", views.OrderItemView.as_view()),
]
