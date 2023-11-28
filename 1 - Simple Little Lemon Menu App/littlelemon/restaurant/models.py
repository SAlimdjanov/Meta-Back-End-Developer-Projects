"""
models.py

"""

from django.db import models


class Booking(models.Model):
    """Booking model

    Args:
        models (Model): Django model template class

    Returns:
        str: Model object display string
    """

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    # Added to suppress linter warnings
    objects = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Menu(models.Model):
    """Menu model

    Args:
        models (Model): Django model template class
    """

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000, default=" ")

    # Added to suppress linter warnings
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.name)
