"""
apps.py

"""

from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    """Configuration of the 'restaurant' app

    Args:
        AppConfig (django.apps): Django app configuration class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'
