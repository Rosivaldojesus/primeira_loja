from django.db import models

# Create your models here.

class Produtos(models.Model):
    
    STATUS_PRO = (
        (u'ativo', u'Ativo'),
        (u'inativo', u'Inativo'),
    )
    
    
    nome_produto = models.CharField(max_length=50)
    codigo_produto = models.CharField(max_length=10, blank=True, null=True)
    descricao_produto = models.CharField(max_length=200, null=True, blank=True)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img_produto = models.FileField(upload_to='produtos.images/', blank=True)
    status_produto = models.CharField(choices=STATUS_PRO, max_length=10, default=0)