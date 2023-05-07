from django import forms 
from django.forms import ModelForm
from produtos.models import Produtos


class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = [
            'id',
            'nome_produto',
            'codigo_produto',
            'descricao_produto',
            'preco_produto',
            'status_produto',
            'img_produto',
        ]