from django.shortcuts import render
from django.http import HttpResponse
from .models import Continent, State , Flower
from .flowers import flowers as flowers_list

# Create your views here.


def db_init():                                                          # clear all data
    Continent.objects.all().delete()                                    


def db_update(f):                                                       # f = flowers_list
    #print('turple len-->', len(f))
    for i in range(len(f)):                                             
        #print(f[i][0], f[i][1], f[i][2], f[i][3])                      # continent, state, flower, image_link
        
        if not Continent.objects.filter(name=f[i][0]).exists():
            continent = Continent(name=f[i][0])
            continent.save()
        else:
            continent = Continent.objects.get(name=f[i][0])
        
        if not State.objects.filter(name=f[i][1]).exists():
            state = State(continent_id=continent.id, name=f[i][1])
            state.save()
        else:
            state = State.objects.get(name=f[i][1])    
            
        if not Flower.objects.filter(continent_id=continent.id, state_id=state.id, name=f[i][2]).exists():
            flower = Flower(continent_id=continent.id, state_id=state.id, name=f[i][2], image_link=f[i][3])
            flower.save()
        else:
            flower = Flower.objects.filter(continent_id=continent.id, state_id=state.id, name=f[i][2])[0]
            flower.image_link = image_link=f[i][3]
            flower.save()


def db_filter():
    
    continents = Continent.objects.order_by('name')
    states = State.objects.order_by('name')
    flowers = Flower.objects.order_by('continent__name', 'state__name', 'name')

    context = {
        'continents' : continents,
        'states' : states,
        'flowers' : flowers,
    }

    return context


def index(request):
    
    return render(request, 'flowers/index.html', db_filter())


def clear(request):

    db_init()

    return render(request, 'flowers/index.html', db_filter())


def update(request):    

    db_update(flowers_list)

    return render(request, 'flowers/index.html', db_filter())


def continents(request, continent_id):

    context = db_filter()
    context['flowers'] = context['flowers'].filter(continent_id=continent_id)
    
    return render(request, 'flowers/continents.html', context)


def states(request, state_id):

    context = db_filter()
    context['flowers'] = context['flowers'].filter(state_id=state_id)
    
    return render(request, 'flowers/states.html', context)