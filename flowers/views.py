from django.shortcuts import render
from django.http import HttpResponse
from .models import Continent, State , Flower
from .flowers import flowers as flowers_list

# Create your views here.


def db_init():
    Continent.objects.all().delete()


def db_update(f):
    for i in range(len(f)):
        print(f[i][0], f[i][1], f[i][2])                                # continent, state, flower
        
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
            
        flower = Flower(state_id=state.id, name=f[i][2])
        flower.save()



def index(request):

    context = {}

    if request.method == 'POST':
        
        #db_init()
        #db_update(flowers_list)


        flowers = Flower.objects.all()
        flowers_count = flowers.count

        context = {
            'flowers' : flowers,
            'flowers_count' : flowers_count,
        }


    return render(request, 'flowers/index.html', context)
