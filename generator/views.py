import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request , 'generator/home.html' , {"password" : "ali"})
def password(request):

    the_password = "testing"

    characters = list("abcdefghijklmnopqrstuvwxyz")

    length = int(request.GET.get("length"))
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))
    the_password = ""
    for x in range(length):
        the_password+= random.choice(characters)
    return render(request , "generator/password.html" , {"password" : the_password})

def about(request):
    return render(request , "generator/about.html")