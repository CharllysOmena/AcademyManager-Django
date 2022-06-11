from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = {'nome', 'matricula', 'cpf'}
        labels = {
            'nome' : 'Nome:', 
            'matricula' : 'Matricula:',
            'cpf' : 'CPF:',
            }