"""
models.py

"""


from django.db import models


class Menu(models.Model):
    """Menu Item Table"""

    # Declare attribute "id" with to overwrite default id primary key of type 'bigint'
    id = models.SmallAutoField(primary_key=True)

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    objects = models.Manager()

    def __str__(self):
        return str(self.title)


class Booking(models.Model):
    """Restaurant Booking Table"""

    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()

    objects = models.Manager()

    def __str__(self):
        return str(self.name)
