from django.db import models
from datetime import datetime

# Create your models here.


class Continent(models.Model):
    name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class State(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name

class Flower(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

