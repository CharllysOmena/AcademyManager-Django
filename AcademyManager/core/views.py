from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# VIEWS DE LOGIN E LOGOUT
@require_http_methods([ 'POST', 'GET'])
def user_login(request):
    if request.user.is_authenticated:
        return redirect('listar_alunos')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_alunos')
        else:
            messages.error(request ,'Usuário ou senha inválidos.')
    return render(request, "login.html")
            
@require_http_methods([ 'POST', 'GET'])
def user_logout(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
    return redirect('login')

# VIEW INICIAL
def index(request):
    return render(request, 'index.html')

