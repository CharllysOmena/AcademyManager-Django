from django import forms
from .models import Aluno, Treino

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