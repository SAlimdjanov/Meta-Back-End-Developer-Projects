"""
models.py

"""


from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Contains food item categories. Enables a client application to search for items based on
    its category"""

    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.title)


class MenuItem(models.Model):
    """Contains information about a particular menu item"""

    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.title)


class Cart(models.Model):
    """Temporary storage for users to add menu items before placing an order. The 'user' field
    ensures that there can only be one cart per user"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    objects = models.Manager()

    class Meta:
        """metadata: There can only be one menu item entry for a specific user"""

        unique_together = ("menu_item", "user")

    def __str__(self) -> str:
        return str(self.user + self.menu_item)


class Order(models.Model):
    """Creates an order from 'Cart' with relevant information"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True
    )
    delivery_status = models.BooleanField(db_index=True, default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.user + self.date)


class OrderItem(models.Model):
    """All items from the cart will be moved here with upon placement of an order. After that, they
    will be deleted"""

    order = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    objects = models.Manager()

    class Meta:
        """metadata: An order can have one menu item with varying quantity"""

        unique_together = ("order", "menu_item")

    def __str__(self) -> str:
        return str(self.menu_item, self.quantity)
