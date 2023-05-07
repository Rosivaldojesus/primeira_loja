from django.db import models, connection
from .models import Produtos


def excluirProduto(self, produto_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM produtos_produtos WHERE id = %s", [produto_id])
    return True
    