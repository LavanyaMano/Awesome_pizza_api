from django.db import models

class Pizza(models.Model):
    pizza_name = models.CharField(max_length =50)
    quantity = models.DecimalField(max_digits=10,decimal_places = 0)
    price = models.DecimalField(max_digits=10,decimal_places = 2)

    def __str__(self):
        return self.pizza_name


