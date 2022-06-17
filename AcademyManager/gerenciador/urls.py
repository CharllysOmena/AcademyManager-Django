from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarAlunos, name='listar_alunos'),
    path('adicionar_alunos', views.adicionarAlunos, name='adicionar_alunos'),
    path('editar_alunos/<int:pk>/', views.editarAlunos, name='editar_alunos'),
    path('excluir_alunos/<int:pk>/', views.excluirAlunos, name='excluir_alunos'),
    path('listar_treinos/<int:pk>/', views.listarTreinos, name='listar_treinos'),
    path('adicionar_treinos', views.adicionarTreinos, name='adicionar_treinos')
]