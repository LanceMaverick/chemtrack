from __future__ import unicode_literals
from django.db import models

class Reagent(models.Model):
    #information is taken from pubchem api and saved in model
    cid = models.IntegerField()
    name = models.CharField(max_length = 100)
    formula = models.CharField(max_length=50)

#liquid and solid reagents are kept in seperate models
#as model fields differ 
class LiquidEntry(models.Model):
    #id number is stored for look-up in reagent table
    #rest is from user filled form or auto generated (e.g date)
    reagent_number = models.ForeignKey(Reagent, on_delete=models.CASCADE)
    date = models.DateField()
    concentration = models.FloatField() #in %
    volume = models.FloatField()   #in ml     
    quantity = models.FloatField() #volume*concentration of entry.

    
class SolidEntry(models.Model):
    reagent_number = models.ForeignKey(Reagent, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField() # in mg

