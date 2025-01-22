from django.shortcuts import render, HttpResponseRedirect
from django import forms
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label='new task')

def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'tasks/index.html', {
        'tasks':request.session['tasks'],
    })

# Add a new task:
def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += task
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            # if the form is invalid giving it back with the existing information
            return render(request, "tasks/add.html", {
                'form':form
            })
    
    return render(request, "tasks/add.html", {
        'form':NewTaskForm()
    })
    
