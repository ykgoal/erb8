from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('continents/<int:continent_id>', views.continents, name='continents'),     
    path('states/<int:state_id>', views.states, name='states'),     
    path('waters', views.waters, name='waters'),            #clear all data 
    path('plants', views.plants, name='plants'),            #update data
]
