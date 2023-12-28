"""
models.py

"""


from django.db import models


class Booking(models.Model):
    """Booking Model"""

    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    objects = models.Manager()

    def __str__(self):
        return str(self.first_name)


class Menu(models.Model):
    """Menu Model"""

    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default="")
    objects = models.Manager()

    def __str__(self):
        return str(self.name)
