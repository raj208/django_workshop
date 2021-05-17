from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('created_date').filter(is_featured = True) #pushing data into fontend
    all_cars = Car.objects.order_by('created_date')
    data = {
    'teams' : teams,
    'featured_cars': featured_cars,
    'all_cars': all_cars,
    }
    return render(request,'page/home.html',data)

def about(request):     #request= I'm taking the informaation from the browser(url)
    teams = Team.objects.all()
    data = {
    'teams' : teams,
    }
    return render(request, 'page/about.html',data)   #I'm accepting the request toi render to the given page


def services(request):
    return render(request, 'page/services.html')

def contact(request):
    return render(request, 'page/contact.html')
