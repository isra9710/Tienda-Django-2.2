from .models import Cart
def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None #Si el usuario está autenticado, obtenemos el usuario actual, de otro modo, None
    cart_id = request.session.get('cart_id') #Intentamos obtener el valor de cart_id, si la llave no existe, es None
    cart = Cart.objects.filter(cart_id=cart_id).first()#Intentamos obtener el carrito de compras a tráves de cart_id o None
    if cart is None:#Si el carrito no existe podemos crear uno nuevo
        cart = Cart.objects.create(user=user)
        
    if user and cart.user is None: #Asignar carrito a usuario
        cart.user = user
        cart.save()
    request.session['cart_id'] = cart.cart_id#Actualizar sesión
    return cart