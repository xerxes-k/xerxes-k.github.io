from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("<int:flight_id>/book", views.book, name="book"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("/login", views.login_view, name="login"),
    path("/logout", views.logout_view, name="logout"),   
]
