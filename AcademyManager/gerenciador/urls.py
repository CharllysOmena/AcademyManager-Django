from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarAlunos, name='listar_alunos'),
    path('adicionar_alunos', views.adicionarAlunos, name='adicionar_alunos'),
    path('editar_alunos/<int:pk>/', views.editarAlunos, name='editar_alunos'),
    path('excluir_alunos/<int:pk>/', views.excluirAlunos, name='excluir_alunos'),
    path('listar_treinos/<int:pk>/', views.listarTreinos, name='listar_treinos'),
    path('adicionar_treinos/<int:pk>/', views.adicionarTreinos, name='adicionar_treinos'),
    path('excluir_treinos/<int:pk>/', views.excluirTreinos, name='excluir_treinos'),
    path('editar_treinos/<int:pk>/', views.editarTreinos, name='editar_treinos'),
    path('listar_exercicios/<int:pk>/', views.listarExercicios, name='listar_exercicios'),
    path('adicionar_exercicios/<int:pk>/', views.adicionarExercicios, name='adicionar_exercicios'),
    path('editar_exercicios/<int:pk>/', views.editarExercicios, name='editar_exercicios'),
    path('excluir_exercicios/<int:pk>/', views.excluirExercicios, name='excluir_exercicios'),
]