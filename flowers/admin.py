from django.contrib import admin
from .models import Continent, State , Flower


# Register your models here.



class ContinentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publish_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Continent, ContinentAdmin)



class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'continent', 'name', 'publish_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(State, StateAdmin)



class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'name', 'image_link', 'publish_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Flower, FlowerAdmin)
