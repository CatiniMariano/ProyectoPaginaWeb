from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.forms import *
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.edit import FormMixin
from .models import *

@login_required
def editarblog(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST': 
        form = CrearBlogFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            blog.tittle= info["tittle"]
            blog.subtitle= info["subtitle"]
            blog.descr= info["descr"]
            blog.relleno= info["relleno"]
            blog.imagen= info["imagen"]
            blog.save()
            blog= Blog.objects.all()
            return render(request, 'paginas/blog.html', {'blogs': blog})
        pass


    else:
        form= CrearBlogFormulario(initial=
        {"tittle": blog.tittle,
         "subtitle": blog.subtitle,
         'descr': blog.descr,
         'relleno': blog.relleno,
         'usuario': blog.usuario,
         'imagen': blog.imagen
        })
        return render(request, 'paginas/editarblog.html', {'form': form, 'blog': blog})
@login_required
def crearblog(request):
    if request.method == 'POST':
        form = CrearBlogFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            blog = Blog ( 
            tittle = info['tittle'],
            subtitle = info['subtitle'],
            descr = info['descr'],
            relleno = info['relleno'],
            usuario= info['usuario'],
            imagen= info['imagen'],
            )
            blog.save()
            return render(request, 'paginas/inicio.html')
        else: 
            return render(request, 'paginas/crearblog.html', {'form': form})
    else: 
        form = CrearBlogFormulario()
        return render(request, 'paginas/crearblog.html', {'form': form})

@login_required       
def eliminarblog(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    blog = Blog.objects.all()
    return render (request,'paginas/blog.html', {'blogs': blog})

    
    

    



def detallepost(request, id):
    blog = Blog.objects.get(id=id)
    
    return render(request, 'paginas/post.html',{'detalle_post':blog})

def blog(request):
    blogs = Blog.objects.filter()
    return render (request,'paginas/blog.html',{'blogs': blogs })
def inicio(request):
    return render (request,'paginas/inicio.html')
def registro(request):
    if request.method == 'POST':
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request,'paginas/inicio.html',{"mensaje":f"El usuario {username} fue creado corretamente"})
        else:
            return render(request,'paginas/registro.html',{"mensaje": "No se pudo crear el usuario, intentelo nuevamente"})

    else:
        form = RegistroUsuarioForm()
        return render(request,'paginas/registro.html', {"form": form})


    return render (request,'paginas/registro.html')
def ingreso(request):
        if request.method == 'POST':
            form=AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                info=form.cleaned_data
                usuario=info['username']
                password=info['password']
                verificacion_de_existencia_de_usuario=authenticate(username=usuario, password=password)
                if verificacion_de_existencia_de_usuario is not None:
                    login( request , verificacion_de_existencia_de_usuario)
                    return render(request,'paginas/inicio.html',{"mensaje":f"Bienvendio {usuario}, logueado correctamente"})
                else:
                    return render(request,'paginas/login.html',{"form":form,"mensaje":"Usuario o contraseña incorrectos"})
            else:
                return render(request,'paginas/login.html',{"form":form,"mensaje":"Usuario o contraseña incorrectos"})

        else:
            form = AuthenticationForm()
            return render(request,'paginas/login.html',{"form": form})

def sobremi(request):
    return render (request,'paginas/sobremi.html')

@login_required
def editarperfil(request):
    usuario=request.user

    if request.method=='POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render (request,'paginas/editarperfil.html',{"mensaje" : f"Editado correctamente"})
        else:
            return render (request,'paginas/editarperfil.html',{"form": form})
    else:
        form = UserEditForm(instance = usuario)
        return render (request,'paginas/editarperfil.html',{"form": form})