from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produtos import views

urlpatterns = [
    path('', views.homeProdutos, name='homeProdutos'),
    path('cadastrarProdutos/', views.cadastrarProdutos, name='cadastrarProdutos'),
    path('editarProduto/<int:produto_id>/', views.editarProduto, name='editarProduto'),
    path('salvarAlteracoesProduto/<int:produto_id>/', views.salvarAlteracoesProduto, name='salvarAlteracoesProduto'), 
    path('deleteProduto<int:produto_id>/', views.deleteProduto, name="deleteProduto"),  
    path('ativarProduto/', views.ativarProduto, name="ativarProduto"), 
    path('salvarAtivarProduto/', views.salvarAtivarProduto, name="salvarAtivarProduto"),
]
