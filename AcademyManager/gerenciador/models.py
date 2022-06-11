from localflavor.br.models import BRCPFField
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField(unique=True, blank=False)
    cpf = BRCPFField('CPF')


