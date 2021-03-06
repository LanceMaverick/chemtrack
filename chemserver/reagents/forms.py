from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
from reagents.models import SolidEntry, LiquidEntry, Reagent

#test class
class NewReagentSearch(forms.Form):
    reagent_name = forms.CharField(required=True)

class AddNewReagent(forms.Form):
    def __init__(self, *args, **kwargs):
        results = kwargs.pop('results')
        super(AddNewReagent, self).__init__(*args, **kwargs)
        CHOICES = [(r['cid'], str(r['name'])) for r in results]
        self.fields['choose'].widget = forms.RadioSelect()
        self.fields['choose'].choices = CHOICES
        
        

class AddReagentForm(ModelForm):
    class Meta:
        model = Reagent
        fields = ['name', 'formula']
        
#    choose = forms.ChoiceField() 


#model form for adding use entry
class SolidEntryForm(ModelForm):
    class Meta:
        model = SolidEntry
        fields = ['reagent', 'quantity']


class LiquidEntryForm(ModelForm):
    class Meta:
        model = LiquidEntry
        fields = ['reagent', 'volume', 'concentration']


class UserRegForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
