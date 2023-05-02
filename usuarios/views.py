from django.shortcuts import render, redirect
from usuarios.forms import RegistrationForm
from django.contrib.auth import  logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'index.html')


def users(request):
    return render(request, 'users.html')


def cadastrarUsuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
        else:
            form = RegistrationForm()
            context = {
                'form': form,
            }
            return render(request, "cadastarUsuario.html", context)
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, "cadastrarUsuario.html", context)
    

def user_logout(request):
    logout(request)
    return redirect('/')



def alterarSenha(request):
    # language = getIdiomaSystem(request)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, "index.html")
        else:
            return redirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form,
            # 'language': language
        }
    return render(request, "alterarSenha.html", context)