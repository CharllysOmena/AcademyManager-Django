from localflavor.br.models import BRCPFField
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    matricula = models.IntegerField(unique=True, blank=False)
    cpf = BRCPFField('CPF')

class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=False)
    tipo = models.CharField(max_length=1, blank=False)
    regiao = models.CharField(max_length=50, blank=False)

class Exercicio(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=False)
    series = models.IntegerField(blank=False)
    repeticoes = models.IntegerField(blank=False)




