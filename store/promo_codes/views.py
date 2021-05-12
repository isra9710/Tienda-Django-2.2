from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def validate(request):
    return JsonResponse({
        'name':'Israel',
        'job':'Estudiante',
        'courses':[
            {'title':'Django 2.2'},
            {'title':'Flask'},
            {'title':'SQLAlchemy'},
        ]
            
        
    })