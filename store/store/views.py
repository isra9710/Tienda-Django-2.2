from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from products.models import Product


def index(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'index.html', {
        'message': 'Listado de productos',
        'tittle': 'Productos',
        'products': products,
        
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
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
    
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión')
    return redirect('login')


def register(request):
    """form = RegisterForm({#Valores predeterminados para un formulario
        'username':'Israel',
        'email':'isra.rios.con@gmail.com',
    })"""
    if request.user.is_authenticated:
        return redirect('index')
    form = RegisterForm(request.POST or None)#Si la petición es por método POST, genera un formulario con los datos que el cliente está enviando, de otro modo, genera uno con los campos vacíos
    if request.method == 'POST' and form.is_valid():
        """username = form.cleaned_data.get('username')#Diccionario
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)"""
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
        
    return render(request, 'users/register.html',{
        'form':form
    })