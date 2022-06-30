from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import AlunoForm, ExercicioForm, TreinoForm
from .models import Aluno, Exercicio, Treino
from core import utils

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
        'treinos' : treino,
        'pk' : pk
    }
    return render(request, 'listarTreino.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def adicionarTreinos(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    treino = Treino(aluno = aluno)
    form = TreinoForm(request.POST or None, instance=treino)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('listar_treinos', kwargs={'pk' : pk }))
        else:
            return redirect(reverse('adicionar_treinos', kwargs={'pk' : pk }))
    else:
        return render(request, 'adicionarTreino.html', context = {'form':form, 'treino': treino, 'aluno' : aluno})

@require_http_methods(['GET', 'POST'])
@login_required
def editarTreinos(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    form = TreinoForm(request.POST or None, instance=treino)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('listar_treinos', kwargs={'pk' : treino.aluno.id }))
        else:
            return redirect(reverse('editar_treinos', kwargs={'pk' : treino.id }))
    else:
        return render(request, 'adicionarTreino.html', context = {'form':form, 'treino': treino})

@require_http_methods(['GET'])
@login_required
def excluirTreinos(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    treino.delete()
    return redirect(reverse('listar_treinos', kwargs={'pk' : treino.aluno.id }))

#Exercicio

@require_http_methods(['GET'])
@login_required
def listarExercicios(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    exercicio = Exercicio.objects.filter(treino_id = treino)
    context = {
        'treinos' : treino,
        'exercicios' : exercicio,
        'pk': pk
    }
    return render(request, 'listarExercicio.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def adicionarExercicios(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    exercicio = Exercicio( treino = treino)
    form = ExercicioForm(request.POST or None, instance=exercicio)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('listar_exercicios', kwargs={'pk' : pk }))
        else:
            return redirect(reverse('adicionar_exercicios', kwargs={'pk' : pk }))
    else:
        return render(request, 'adicionarExercicio.html', context = {'treinos': treino, 'form': form, 'exercicios':exercicio})

@require_http_methods(['GET', 'POST'])
@login_required
def editarExercicios(request, pk):
    exercicio = get_object_or_404(Exercicio, pk=pk)
    form = ExercicioForm(request.POST or None, instance = exercicio)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('listar_exercicios', kwargs={'pk' : exercicio.treino.id}))
        else:
            return redirect(reverse('adicionar_exercicios', kwargs={'pk' : exercicio.id}))
    else:
        return render(request, 'adicionarExercicio.html', context={'exercicio' : exercicio, 'form': form})

@require_http_methods(['GET'])
@login_required
def excluirExercicios(request, pk):
    exercicio = get_object_or_404(Exercicio, pk=pk)
    exercicio.delete()
    return redirect(reverse('listar_exercicios'), kwargs = {'pk' : pk})

# Acesso do aluno

@require_http_methods(['GET'])
def areaDoAluno(request):
    return render(request, 'areadoaluno.html')

@require_http_methods(["GET"])
def buscarAlunos(request):
    form = AlunoForm(request.POST or None)
    pesquisa = request.GET['pesquisa']
    filtro = utils.montador_de_filtro(Aluno, ['nome', 'matricula', 'cpf'], pesquisa)
    aluno = Aluno.objects.filter(filtro)
    context = {
        'pesquisa' : pesquisa,
        'alunos' : aluno,
        'form' : form
    }
    return render(request, 'aluno.html', context)

@require_http_methods(['GET'])
def treinos(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    treino = Treino.objects.filter(aluno_id = aluno)
    context = {
        'aluno' : aluno,
        'treinos' : treino,
        'pk' : pk
    }
    return render(request, 'treino.html', context)

@require_http_methods(['GET'])
def exercicios(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    exercicio = Exercicio.objects.filter(treino_id = treino)
    context = {
        'treinos' : treino,
        'exercicios' : exercicio,
        'pk': pk
    }
    return render(request, 'exercicio.html', context)
