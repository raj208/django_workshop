from django.contrib import admin
from .models import Car
from django.utils.html import format_html #this makes html work in python files, thus we can work using html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):  # this function makes  thumbnail(putting photo)
        return format_html('<img src = "{}" width ="100" style ="border_radius:100px"/>'.format(object.car_photo.url))
        thumbnail.short_description = 'car_photo'
    list_display = ('id', 'car_title',"thumbnail",'state','model','color','body_style','fuel_type','is_featured')
    list_display_links = ("id", "car_title","thumbnail")  #making clickable
    search_fields = ("id","car_title", "model","body_style","fuel_type") #making search function
    list_filter = ("model","fuel_type","body_style")  #filtering
    list_editable = ('is_featured',)


admin.site.register(Car, CarAdmin)
