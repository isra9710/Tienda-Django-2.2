from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart(request):
    request.session['cart_id'] = None
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(cart_id=cart_id)#Obtenemos el carrito de base de datos
        if cart is None:#Si no se ha creado un carrito
            cart = Cart.objects.create(user=user)
    else:
        cart = Cart.objects.create(user=user)
    request.session['cart_id'] = cart.cart_id
    return render(request, 'carts/cart.html')