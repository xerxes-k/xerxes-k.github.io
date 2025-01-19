from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label='new task')

tasks = ['tester', 'pppppy', 'lecture3']

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks':tasks,
    })

# Add a new task:
def add(request):
    return render(request, "tasks/add.html", {
        'form':NewTaskForm()
    })