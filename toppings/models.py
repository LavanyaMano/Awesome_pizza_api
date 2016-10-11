from django.db import models

class Topping(models.Model):
    topping = models.CharField(max_length =50)
    price = models.DecimalField(max_digits=10,decimal_places = 2)
    basepizza = models.ForeignKey('pizza.Pizza')
    
    def __str__(self):
        return self.topping


