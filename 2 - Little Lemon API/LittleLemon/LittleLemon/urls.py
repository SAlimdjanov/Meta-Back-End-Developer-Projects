"""
urls.py

URL configuration for the LittleLemon project

"""


from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView


# Inherit the 'TokenObtainPairView' view to rename the header and description in the browsable API
# view.
class LoginTokensView(TokenObtainPairView):
    "Generate access tokens to be used in other API calls"


urlpatterns = [
    path("", include("djoser.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("LittleLemonAPI.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("token/login", LoginTokensView.as_view()),
]
