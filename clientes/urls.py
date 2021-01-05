from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('minhas_vacinas/', views.vacina, name='vacina'),
    path('minhas_consultas/', views.consulta, name='consulta'),
    path('minhas_cirurgias/', views.cirurgia, name='cirurgia'),
    path('<int:animal_id>', views.ver_animal, name='ver_animal'),
    path('clientes/<int:tutor_id>', views.ver_cliente, name='ver_cliente'),
    path('minhas_vacinas/<int:vacina_id>', views.ver_vacina, name='ver_vacina'),
    path('minhas_consultas/<int:consulta_id>', views.ver_consulta, name='ver_consulta'),
    path('minhas_cirurgias/<int:cirurgia_id>', views.ver_cirurgia, name='ver_cirurgia'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'), 
    path('criar_cliente/', views.criarCliente, name='criar_cliente'), 
    path('atualizar_cliente/<str:pk>/', views.atualizarCliente, name='atualizar_cliente'),
    path('deletar_cliente/<str:pk>/', views.deletarCliente, name='deletar_cliente'),
    path('criar_animal/', views.criarAnimal, name='criar_animal'), 
    path('atualizar_animal/<str:pk>/', views.atualizarAnimal, name='atualizar_animal'),
    path('deletar_animal/<str:pk>/', views.deletarAnimal, name='deletar_animal'),
    path('criar_vacina/', views.criarVacina, name='criar_vacina'),
    path('atualizar_vacina/<str:pk>/', views.atualizarVacina, name='atualizar_vacina'),
    path('deletar_vacina/<str:pk>/', views.deletarVacina, name='deletar_vacina'),
]