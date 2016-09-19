from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^search/$', views.reagent_search, name='reagent_search'),
        url(r'^add_reagent/$', views.add_reagent, name='add_reagent'),
        url(r'^results/(?P<results>[\w\-]+)/$', views.reagent_results, name='results'),
        url(r'^add_solid/$', views.add_solid_entry, name = 'add_solid'),
        url(r'^add_liquid/$', views.add_liquid_entry, name = 'add_liquid'),
        url(r'^summary/$', views.show_entries, name = 'summary'),
        ]
