from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    now = datetime.now()
    # return HttpResponse("<h1 style='color:red'> newyear <h1>")
    return render(request, 'newyear/index.html', {
        "newyear" : now.month == 1 and now.day == 1
    })