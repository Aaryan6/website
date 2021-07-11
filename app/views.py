from django.shortcuts import render
from .models import Htmldata, Pythondata, Pygamedata
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def htmlpage(request):
    htmldata = Htmldata.objects.all()
    return render(request, 'html-projects.html',{'code':htmldata})

def pythonpage(request):
    pythondata = Pythondata.objects.all()
    return render(request, 'python-projects.html',{'code':pythondata})

def pygamepage(request):
    pygamedata = Pygamedata.objects.all()
    return render(request, 'pygame-projects.html',{'code':pygamedata})

def videospage(request):
    return render(request, 'videos.html')

def html_cheatsheet(request, id):
    htmlcodes = Htmldata.objects.filter(code_id = id)[0]
    return render(request, 'html_cheatsheet.html',{'sheet':htmlcodes})

def python_cheatsheet(request, id):
    python_codes = Pythondata.objects.filter(code_id = id)[0]
    return render(request, 'python_cheatsheet.html',{'pysheet':python_codes})

def pygame_cheatsheet(request, id):
    pygame_codes = Pygamedata.objects.filter(code_id = id)[0]
    return render(request, 'pygame_cheatsheet.html',{'pygamesheet':pygame_codes})
