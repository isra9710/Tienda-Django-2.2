from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
def index(request):
    return render(request, 'index.html', {
        'message': 'Listado de productos',
        'tittle': 'Productos',
        'products': [
            {'tittle': 'Playera', 'price': 5, 'stock': True},  # producto
            {'tittle': 'Camisa', 'price': 7, 'stock': True},
            {'tittle': 'Mochila', 'price': 20, 'stock': False},
            {'tittle': 'Laptop', 'price': 500, 'stock': False},
        ]
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #El atributo POST es un diccionario
        password = request.POST.get('password') #Por eso podemos usar el método get, como argumento mandamos la clave que deseamos obtener
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvendio {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
    return render(request,'users/login.html',{
        
    })