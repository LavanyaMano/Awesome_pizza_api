from rest_framework import serializers 
from .models import Pizza




class PizzaSerializer(serializers.ModelSerializer):
    totalprice = serializers.SerializerMethodField(read_only = True)
    def toppingprice (self,pizza):
        topping_totalprice = 0
        for topping in pizza.topping_set.all():
            topping_totalprice+=topping.price
        return topping_totalprice

    def get_totalprice (self,pizza):
        return (pizza.price + self.toppingprice(pizza))*pizza.quantity

    class Meta:
        model = Pizza
        fields = (
            'id',
            'pizza_name',
            'quantity',
            'price',
            'totalprice',
            )
