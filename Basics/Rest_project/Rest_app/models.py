from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    unit_price = models.FloatField(max_length=10000)
    date_added = models.DateTimeField(auto_created=True)

    def __str__(self) -> str:
        return self.title


