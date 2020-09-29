from django.db import models


class Customer(models.Model):
    """
    Customer
    """
    name = models.CharField(max_length=100)
