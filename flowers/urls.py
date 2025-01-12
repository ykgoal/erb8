from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('clear', views.clear, name='clear'), 
    path('update', views.update, name='update'),
    path('continents/<int:continent_id>', views.continents, name='continents'),     
    path('states/<int:state_id>', views.states, name='states'),   
]
