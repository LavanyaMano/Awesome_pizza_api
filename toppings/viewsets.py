from rest_framework import viewsets
from .models import Topping
from .serializers import ToppingSerializer

class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q',None)
        if query:
            self.queryset = self.queryset.filter(topping__icontains= query)
        return self.queryset