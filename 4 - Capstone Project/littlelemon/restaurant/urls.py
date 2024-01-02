"""
urls.py

"""

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api-token-auth/", obtain_auth_token),
    path("menu/", views.MenuItemView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
]
