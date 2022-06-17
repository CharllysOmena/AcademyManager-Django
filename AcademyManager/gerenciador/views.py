from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .forms import AlunoForm, TreinoForm
from .models import Aluno, Treino

#Aluno

@require_http_methods(['GET'])
@login_required
def listarAlunos(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos,
    }
    return render(request, 'listarAlunos.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def adicionarAlunos(request):
    form = AlunoForm(request.POST or None)
    context = {
        'form' : form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
        else:
            messages.error(request, 'Formulário invalido, Verifique os campos!')
            return redirect('adicionar_alunos')
    else:
        return render(request, "adicionarUsuario.html", context)

@require_http_methods(['GET', 'POST'])
@login_required
def editarAlunos(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    context = {
        'form' : form,
        'aluno': aluno,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
        else:
            messages.error(request, 'Formulário invalido, Verifique os campos!')
            return redirect('adicionar_alunos')
    else:
        return render(request, "adicionarUsuario.html", context)

@require_http_methods(['GET'])
@login_required
def excluirAlunos(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.delete()
    return redirect('listar_alunos')

#Treino

@require_http_methods(['GET'])
@login_required
def listarTreinos(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    treino = Treino.objects.filter(aluno_id = aluno)
    context = {
        'aluno' : aluno,
        'treinos' : treino
    }
    return render(request, 'listarTreino.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def adicionarTreinos(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    treino_aluno = Treino(aluno = aluno)
    form = TreinoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_treinos')
        else:
            return redirect('adicionar_treinos')
    else:
        return render(request, 'adicionarTreino.html', context = {'form':form, 'treino_aluno': treino_aluno})





