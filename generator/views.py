from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET['length'])

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()\/{\}|":?><'))


    thePassword = ''
    for value in range(length):
        thePassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': thePassword})

def aboutPage(request):
    return render(request, 'generator/about.html')

