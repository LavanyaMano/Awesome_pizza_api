from rest_framework import viewsets
from .models import Topping
from .serializers import ToppingSerializer

class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer