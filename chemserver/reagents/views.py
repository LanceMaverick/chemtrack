from datetime import datetime
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
#from django.views.generic import ListView, View
from django.views import generic
from django import forms
from . import forms as myforms
from . import  chemquery as cq
from .models import Reagent, LiquidEntry, SolidEntry 


def index(request):
    return render(request, 'reagents/index.html')


def confirm_new_reagent(request, content):
    if 'confirm' in request.POST:
        entry = Reagent.objects.create(**content)
        return render(request,  'reagents/reagent_confirmed.html', 
                {'entry': entry}) 
    #check for matches in db to avoid repeat entries:
    matches = Reagent.objects.filter(
            formula__iexact=content['formula'])
    variables = {'content': content, 'matches': matches}
    return render(request, 'reagents/confirm_reagent.html',
            variables)


class AddEntryView(SuccessMessageMixin, generic.edit.CreateView):
    template_name = 'reagents/generic_form.html'
   
    def form_valid(self, form):
        self.object = form.save()
        info = 'Entry "{}" added successfully!'.format(str(self.object))
        return self.render_to_response(self.get_context_data(
                form=form, info=info)) 


#TODO generic month summary class that gets model from kwargs
class MonthlySummarySolid(generic.dates.MonthArchiveView):
    queryset = SolidEntry.objects.all()
    date_field = 'date'


class MonthlySummaryLiquid(generic.dates.MonthArchiveView):
    queryset = LiquidEntry.objects.all()
    date_field = 'date'


#TODO: make single general redirect for any model
def show_entries(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    return redirect(
        'month_summary_solid',
        year = current_year,
        month = current_month)


#redirects to month_summary with current month data
#TODO make general for solids and liquids
def show_entries_solid(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    return redirect(
        'month_summary_solid',
        year = current_year,
        month = current_month)


def show_entries_liquid(request):
        current_year = datetime.now().year
        current_month = datetime.now().month
        return redirect(
            'month_summary_liquid',
            year = current_year,
            month = current_month)

#register user
class UserAuthView(generic.View):
    form_class = myforms.UserRegForm
    template_name = 'reagents/generic_form.html'
    
    def get(self, request):
        form= self.form_class(None)
        return render(request, self.template_name, {'form': form})

    
    def post(self, request):
        form= self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user_auth = authenticate(username=username, password=password)

            if user_auth is not None:
                if user_auth.is_active:
                    login(request, user_auth)
                    return redirect('index')
            
        return render(request, self.template_name, {'form': form})


class ReagentListView(generic.ListView):
    template_name = 'reagents/list_base.html' 
    model = Reagent
