"""
apps.py

"""


from django.apps import AppConfig


class LittlelemonapiConfig(AppConfig):
    """Configures API App"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "LittleLemonAPI"
