from django.db import models
from order.models import Order

# Create your models here.


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
