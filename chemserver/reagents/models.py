from __future__ import unicode_literals
from django.db import models

class Reagent(models.Model):
    #information is taken from pubchem api and saved in model
#    cid = models.IntegerField()
    name = models.CharField(max_length = 100)
    formula = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'substances and reagents'
    
    def __str__(self):
        return '{} | {}'.format(self.name, self.formula)
    


#liquid and solid reagents are kept in seperate models
#as model fields differ 
class LiquidEntry(models.Model):
    #id number is stored for look-up in reagent table
    #rest is from user filled form or auto generated (e.g date)
    reagent = models.ForeignKey(Reagent, on_delete=models.CASCADE)
    date = models.DateField(verbose_name = 'date of usage', auto_now_add=True)
    concentration = models.FloatField(verbose_name = 'concentration (%)', null=True) # in%
    volume = models.FloatField(verbose_name = 'quantity used (ml)', null=True)   #in ml     
    
    def _get_quantity(self):
        #volume*concentration of entry.
        return self.volume * self.concentration/100.
    quantity = property(_get_quantity)

    def __str__(self):
        return '{} | {} ml'.format(self.reagent.formula, self.quantity)

    class Meta:
        verbose_name = 'liquid'


class SolidEntry(models.Model):
    reagent = models.ForeignKey(Reagent, on_delete=models.CASCADE)
    date = models.DateField(verbose_name = 'date of usage', auto_now_add=True)
    quantity = models.FloatField(verbose_name =  'amount used in (mg)', null=True) # in mg

    def __str__(self):
        return '{} | {} mg'.format(self.reagent.formula, self.quantity)

    class Meta:
        verbose_name = 'solid'
