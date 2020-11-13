from django.shortcuts import render
from django.http import HttpResponse
from generator import random_password
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'hasdhflsdf'})

def password(request):

    length_int = int(request.GET.get('length'))
    
    special_bool = False 
    if request.GET.get('special'):
        special_bool = True

    numbers_bool = False 
    if request.GET.get('special'):
        numbers_bool = True

    caps_bool = False
    if request.GET.get('capson'):
        caps_bool = True
    
    #separator_str = str(request.GET.get('separator'))

    thepassword = random_password.passphrase(length=length_int, numbers=numbers_bool, special=special_bool, capson=caps_bool, separator='-')
    #thepassword = random_password.passphrase(length=3, numbers=1, special=True, capson=False, separator=separator_str)

    #thepassword = 'testing' 

    #characters = list('abcdefghijklmnopqrstuvwxyz')

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
