from rest_framework import serializers
from .models import Empregado

class EmpregadoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Empregado
        field = '__all__'     # ('id', 'nome') no caso queira campos específicos. 
