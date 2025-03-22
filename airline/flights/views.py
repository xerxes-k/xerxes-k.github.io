from django.shortcuts import render, HttpResponseRedirect
from .models import Flight, Airport, Passenger
from django.urls import reverse

# Additional imports we'll need:
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })
    
    
def book(request, flight_id):
    # For a post request, add a new flight
    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)
        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])
        # Finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)
        # Add passenger to the flight
        passenger.flights.add(flight)
        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'flights/login.html', {
                'message':'invalid credentials'
            })
        
    return render(request, "flights/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'flights/login.html', {
        'message':'logged out'
    })