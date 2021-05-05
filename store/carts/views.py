from django.shortcuts import render

# Create your views here.
def cart(request):
    request.session['cart_id'] = '123'#Crear una sesión
    valor = request.session.get('cart_id') #Obtener el valor de una sesión
    print(valor)
    request.session['cart_id']= None #Eliminar una sesión
    return render(request, 'carts/cart.html')