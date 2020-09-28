from empregadoapi.viewsets import EmpregadoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empregado', EmpregadoViewSet)
