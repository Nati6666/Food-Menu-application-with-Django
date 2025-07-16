from django.db import models


# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_description = models.TextField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
