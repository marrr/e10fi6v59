from django.shortcuts import render
#from glossaire.models import *

def index(request):
    return render(request, 'page/accueil.html')
