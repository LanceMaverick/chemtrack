from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.reagent_search, name='index'),
        url(r'^results/(?P<results>[\w\-]+)/$', views.reagent_results, name='results')
        ]
