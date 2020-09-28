from rest_framework import viewsets
from . import models
from . import serializers

class EmpregadoViewSet(viewsets.ModelViewSet):
    queryset = models.Empregado.objects.all()
    serializer_class = serializers.EmpregadoSerializer()
    
