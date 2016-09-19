from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import ListView
from . import forms as myforms
from . import  chemquery as cq
from .models import Reagent, LiquidEntry, SolidEntry 

def index(request):
    return render(request, 'reagents/index.html')

def reagent_search(request):
    form_class = myforms.NewReagentSearch

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            reagent_name = request.POST.get(
                    'reagent_name','')
           
            results = cq.search_compound(reagent_name)
            return reagent_results(request, results)

    return render(request, 'reagents/generic_form.html', {
        'form': form_class,
        })

def add_reagent(request):
    if request.method == 'GET':
        form = myforms.AddReagentForm()
        return  render(request, 'reagents/generic_form.html',
            {'form': form})

    elif request.method == 'POST':
        form = myforms.AddReagentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            formula = form.cleaned_data['formula']
            content = {'name': name, 'formula': formula}
            return confirm_new_reagent(request, content)

def confirm_new_reagent(request, content):
    if request.method == 'POST':
        print ("HERE") 
        entry = Reagent.objects.create(**content)
        print ("HERE!") 
        return render(request,  'reagents/reagent_confirmed.html', 
                {'entry': entry}) 
    #check for matches in db to avoid repeat entries:
    matches = Reagent.objects.filter(
            formula__iexact=content['formula'])
    variables = {'content': content, 'matches': matches}
    return render(request, 'reagents/confirm_reagent.html',
            variables)

def reagent_results(request, results):
    if not results:
        return HttpResponse('no results found')
    form = myforms.AddNewReagent(data=request.POST, results = results)
    return render(request, 'reagents/choose_reagent.html',{
        'form': form} )

def add_solid_entry(request):
    info = ''
    if request.method == 'GET' :
        form = myforms.SolidEntryForm()
    elif request.method == 'POST':
        form = myforms.SolidEntryForm(request.POST)
        if form.is_valid():
            reagent  = form.cleaned_data['reagent']
            quantity = form.cleaned_data['quantity']
            entry = SolidEntry.objects.create(reagent=reagent, quantity=quantity)
            info = entry
    return render(request, 'reagents/generic_form.html',
            {'form': form, 'info': info})
      
def add_liquid_entry(request):
    info = ''
    if request.method == 'GET' :
        form = myforms.LiquidEntryForm()
    elif request.method == 'POST':
        form = myforms.LiquidEntryForm(request.POST)
        if form.is_valid():
            reagent  = form.cleaned_data['reagent']
            volume = form.cleaned_data['volume']
            concentration = form.cleaned_data['concentration']
            entry = LiquidEntry.objects.create(reagent=reagent, volume=volume, concentration=concentration)
            info = entry
    return render(request, 'reagents/generic_form.html',
            {'form': form, 'info': info})

def show_entries(request):
    solids = SolidEntry.objects.all()
    liquids = LiquidEntry.objects.all()
    context = {'solids': solids, 'liquids': liquids}
    return render(request, 'reagents/entry_table.html', context)
    

