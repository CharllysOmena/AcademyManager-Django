from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarAlunos, name='listar_alunos'),
    path('adicionar_alunos', views.adicionarAlunos, name='adicionar_alunos'),
    path('editar_alunos/<int:pk>/', views.editarAlunos, name='editar_alunos')
]