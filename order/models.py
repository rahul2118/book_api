from django.db import models
from product.models import Book
from user.models import User


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Book)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
