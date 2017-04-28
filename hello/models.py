from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Building(models.Model):
    """
    Model representing a building (but not the history of the building).
    """
    name = models.CharField(max_length=50) # building name
    current = models.IntegerField() # current traffic
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

import uuid # Required for unique book instances

class BuildingInstance(models.Model):
    """
    Model representing a specific moment in the history of the building.
    """
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True) # associated building
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False) # datetime of the measurement
    traffic = models.IntegerField() # traffic at datetime

    class Meta:
        ordering = ["-datetime"] # sort on measurement date
        
    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s %s' % (self.building,self.datetime)