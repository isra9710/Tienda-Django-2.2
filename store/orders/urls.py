from django.urls import path
from . import views
app_name = 'orders'

urlpatterns = [
    path('', views.order, name='order'),
    path('dirección', views.address, name='address')
]