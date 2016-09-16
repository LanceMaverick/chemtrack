from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import NewReagentSearch, AddNewReagent
from . import  chemquery as cq

def index(request):
    return HttpResponse("<h1> Browse reagents</h1>")

def reagent_search(request):
    form_class = NewReagentSearch

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            reagent_name = request.POST.get(
                    'reagent_name','')
           
            results = cq.search_compound(reagent_name)
            return reagent_results(request, results)

    return render(request, 'reagents/add_reagent.html', {
        'form': form_class,
        })

def reagent_results(request, results):
    if not results:
        return HttpResponse('no results found')
    form = AddNewReagent(data=request.POST, results = results)
    #if request.method=='POST':
    #    pass
    print(results)
    return render(request, 'reagents/choose_reagent.html',{
        'form': form}, context_instance=RequestContext(request))


      

