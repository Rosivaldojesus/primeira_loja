from django.shortcuts import render, redirect
from produtos.models import Produtos
from produtos.forms import ProdutosForm
from .functions import excluirProduto

# Create your views here.

def homeProdutos(request):
    produtos = Produtos.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, "produtos.html", context)


def cadastrarProdutos(request):
    form = ProdutosForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = ProdutosForm(request.POST, request.FILES)
        print("form is not valid")
        # print(form.error)
    context = {
        'form':form
    }
    return render(request, "cadastrarProdutos.html", context)


def editarProduto(request, produto_id):
    produto = Produtos.objects.get(id=produto_id)
    context = {
        'produto': produto
    }
    return render(request, 'editarProduto.html', context)


def salvarAlteracoesProduto(request, produto_id):
    produto = Produtos.objects.get(id=produto_id)
    
    nome_produto = request.POST.get("nome_produto")
    codigo_produto = request.POST.get("codigo_produto")
    descricao_produto = request.POST.get("descricao_produto")
    preco_produto = request.POST.get("preco_produto")
    status_produto = request.POST.get("status_produto")
    img_produto = request.FILES.get("img_produto")
    
    produto.nome_produto = nome_produto
    produto.codigo_produto = codigo_produto
    produto.descricao_produto = descricao_produto
    produto.preco_produto = preco_produto
    produto.status_produto = status_produto
    
    if img_produto:
        produto.img_produto = img_produto
        
    produto.save()
    
    return redirect("/produtos/")


def deleteProduto(request, produto_id):
    excluir = excluirProduto(request, produto_id)
    return redirect('/produtos/')


def ativarProduto(request):
    produtos = Produtos.objects.filter(status_produto='inativo')
    context = {
        'produtos': produtos
    }
    return render(request, "ativarProduto.html", context)


def salvarAtivarProduto(request):
    produto_id = request.POST.get("nome_produto")
    produto = Produtos.objects.get(id=produto_id)
    status_produto = request.POST.get("status_produto")
    produto.status_produto = status_produto
    print(produto)
    produto.save()
    return redirect('/produtos/')