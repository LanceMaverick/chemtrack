from django import forms

#class ReagentForm(forms.Form)
#    name =  


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

    choose = forms.ChoiceField() 
    
