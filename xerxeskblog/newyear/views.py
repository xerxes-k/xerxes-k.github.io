from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1 style='color:red'> newyear <h1>")
    # return render(request, 'tester/index.html')