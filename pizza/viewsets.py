from rest_framework import viewsets
from .models import Pizza
from .serializers import PizzaSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    def get_queryset(self):
        query = self.request.query_params.get('q',None)
        if query:
            self.queryset = self.queryset.filter(pizza_name__icontains= query)
        return self.queryset


