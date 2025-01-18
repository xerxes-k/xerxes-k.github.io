from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    
    # the url path is a string, and it's variable name is 'name'
    path("<str:name>", views.greet, name = 'greet'),
]
