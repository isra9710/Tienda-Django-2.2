from django.shortcuts import render

# Create your views here.
def cart(request):
    user = request.user if request.user.is_authenticated else None
    if request.session.get('cart_id'):
        cart = Cart.objects.get(pk=request.session.get('cart_id'))#Obtenemos el carrito de base de datos
    else:
        cart = Cart.objects.create(user=user)
    request.session['cart_id'] = cart.id
    return render(request, 'carts/cart.html')