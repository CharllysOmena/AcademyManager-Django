from django import forms
from .models import Aluno, Exercicio, Treino

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = {'nome', 'matricula', 'cpf'}
        labels = {
            'nome' : 'Nome:', 
            'matricula' : 'Matricula:',
            'cpf' : 'CPF:',
            }

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = {'nome', 'tipo', 'regiao'}
        labels = {
            'nome' : 'Nome:',
            'tipo' : 'Tipo:',
            'regiao' : 'Região:'
        }

class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = {'nome', 'series', 'repeticoes' }
        labels = {
            'nome' : 'Nome do exercicio: ',
            'series' : 'Numéro de series: ',
            'repeticoes' : 'Numéro de repetições: '
        }