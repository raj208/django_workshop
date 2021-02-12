from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about', views.about, name='about'),  #these names are used in html file{% urls 'about' %}
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),

]