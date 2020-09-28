from django.db import models

# Create your models here.

class Empregado(models.Model):
    nome = models.CharField(max_length=100)
    Emp_cd = models.CharField(max_length=4)
    cpf = models.CharField(max_length=11)
    celular = models.CharField(max_length=12)
    