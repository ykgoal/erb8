from django.shortcuts import render
from .models import Continent, State , Flower
from .flowers import flowers as flowers_list

# Create your views here.


def db_init():                                                          # clear all data
    Continent.objects.all().delete()                                    


def db_update(f):                                                       # f = flowers_list
    #print('turple len-->', len(f))
    for i in range(len(f)):                                             
        #print(f[i][0], f[i][1], f[i][2], f[i][3])                      # continent, state, flower, image_link
        
        if Continent.objects.filter(name=f[i][0]).exists():
            continent = Continent.objects.get(name=f[i][0])
        else:
            continent = Continent.objects.create(name=f[i][0])

        if State.objects.filter(name=f[i][1]).exists():
            state = State.objects.get(name=f[i][1]) 
        else:
            state = State.objects.create(continent_id=continent.id, name=f[i][1])
            
        if Flower.objects.filter(state_id=state.id, name=f[i][2]).exists():
            flower = Flower.objects.get(state_id=state.id, name=f[i][2])
            flower.image_link = f[i][3]
            flower.save()
        else:
            flower = Flower.objects.create(state_id=state.id, name=f[i][2], image_link=f[i][3])



def db_filter():
    
    continents = Continent.objects.order_by('name')
    states = State.objects.order_by('name')
    flowers = Flower.objects.order_by('state__continent__name', 'state__name', 'name')

    context = {
        'continents' : continents,
        'states' : states,
        'flowers' : flowers,
    }

    return context


def index(request):
    
    return render(request, 'flowers/index.html', db_filter())


def waters(request):                        #clear all data

    db_init()

    return render(request, 'flowers/index.html', db_filter())


def plants(request):                        #update data

    db_update(flowers_list)

    return render(request, 'flowers/index.html', db_filter())


def continents(request, continent_id):

    context = db_filter()
    context['flowers'] = context['flowers'].filter(state__continent__id=continent_id)
    
    return render(request, 'flowers/continents.html', context)


def states(request, state_id):

    context = db_filter()
    context['flowers'] = context['flowers'].filter(state_id=state_id)
    
    return render(request, 'flowers/states.html', context)