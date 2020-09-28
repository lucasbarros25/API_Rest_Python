# Esse arquivo é uma parte importante da Api, ele serve pra converter a informação para um JSON para
# poder mandar a informação para o que quer que seja. 
from rest_framework import serializers
from .models import Empregado

Class EmpregadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empregado
        field = '__all__' # Se quiser só um ou outro campo é só usar: ('id', 'name')