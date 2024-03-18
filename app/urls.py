from django.urls import path
from . import views

urlpatterns = [
    path('', views.lembrei),
    path('ver_usuarios/', views.ver, name='ver'),
    path('cadastrar_usuario/', views.cadastrar, name='cadastrar'),
    path('atualizar_cadastro/<int:pk>/', views.atualizar, name='atualizar'),
    path('deletar_usuario/', views.deletar, name='deletar')
]
