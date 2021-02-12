from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'page/home.html')

def about(request):     #reuest= I'm taking the informaation from the browser(url)
    return render(request, 'page/about.html')   #I'm accepting the request toi render to the given page


def services(request):
    return render(request, 'page/services.html')

def contact(request):
    return render(request, 'page/contact.html')
