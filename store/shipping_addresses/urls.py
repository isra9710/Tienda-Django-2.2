from django.urls import path 
from . import views
app_name = 'shipping_addresses'

url_patterns = [
    path('', views.ShippingAddressListView.as_view(), name='shipping_addresses'),
]