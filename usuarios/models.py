from django.db import models
from django.contrib.auth.models import User



class Usuario(User):
    matricula = models.CharField("Matrícula", max_length=9, unique=True) 
    saldo = models.IntegerField('Saldo',default=0)
    

