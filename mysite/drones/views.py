from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hola Mundo</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')

def prices(request):
    return HttpResponse('<h1>Precios</h1>')

def tracker(request):
    return HttpResponse('<h1>Rastreador</h1>')
