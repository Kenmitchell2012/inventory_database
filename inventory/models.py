from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    lot_number = models.CharField(max_length=50, blank=False, null=False)
    expiration_date = models.DateField(max_length=100)

    def __str__(self):
        return self.name