from django.urls import path
from .views import listar_contatos, criar_contato, alterar_contato, deletar_contato

urlpatterns = [
    path('', listar_contatos, name='listar_contatos'),
    path('listar_contatos', listar_contatos, name='listar_contatos'),
    path('novo_contato/', criar_contato, name='criar_contato'),
    path('alterar_contato/<int:id>/', alterar_contato, name='alterar_contato'),
    path('deletar_contato/<int:id>/', deletar_contato, name='deletar_contato'),
]