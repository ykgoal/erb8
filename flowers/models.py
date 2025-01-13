from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Continent(models.Model):
    name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

class State(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.name

class Flower(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_link = models.CharField(max_length=200, blank=True)    
    publish_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

