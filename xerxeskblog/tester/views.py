from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("<h1 style='color:red'> testing <h1>")
    return render(request, 'tester/index.html')

def greet(request, name):
    return render(request, 'tester/greet.html', {
        "name" : name.capitalize()
    })