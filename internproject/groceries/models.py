from django.db import models

class grocery_items(models.Model):
    name = models.CharField(max_length=128,unique=True)
    company = models.CharField(max_length=64)
    quantity = models.IntegerField()
    amount = models.CharField(max_length=128,default=100000)

    def __str__(self):
        return self.name