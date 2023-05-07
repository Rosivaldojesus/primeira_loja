from django.contrib import admin
from produtos.models import Produtos

# Register your models here.

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'codigo_produto' , 'descricao_produto', 'preco_produto', 'img_produto',)
    search_fields = ['nome_produto']
    list_filter = ['status_produto']
    save_on_top = True
    