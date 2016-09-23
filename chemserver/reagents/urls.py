from django.conf.urls import url
from . import views
from .models import Reagent, LiquidEntry, SolidEntry
from .forms import AddReagentForm, LiquidEntryForm, SolidEntryForm

urlpatterns = [
        url(r'^$', views.index, name='index'),
        
        url(r'^add/solid/$', views.AddEntryView.as_view(
            model=SolidEntry, form_class = SolidEntryForm), 
            name = 'add_solid'),
        
        url(r'^add/liquid/$', views.AddEntryView.as_view(
            model=LiquidEntry, form_class = LiquidEntryForm), 
            name = 'add_liquid'),
        
        url(r'^add/reagent/$', views.AddEntryView.as_view(
            model=Reagent, form_class = AddReagentForm),
            name = 'add_reagent'),
        
        #TODO: implement model choosing logic in CBV for something like this:
        #url(r'^add/(?P<mtype>.*)/$', views.AddEntryView.as_view(), name = 'add_entry'),
        
        url(r'^summary/solid/$', views.show_entries_solid, name = 'summary_solid'),
        
        url(r'^summary/liquid/$', views.show_entries_liquid, name = 'summary_liquid'),
        
        url(r'^month_summary/solid/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
            views.MonthlySummarySolid.as_view(
                month_format = '%m', template_name = 'reagents/entry_table_solids.html'), 
                name = 'month_summary_solid'),
        
        url(r'^month_summary/liquid/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
            views.MonthlySummaryLiquid.as_view(
                month_format = '%m', template_name = 'reagents/entry_table_liquids.html'), 
            name = 'month_summary_liquid'),
        
        url(r'^register/$', views.UserAuthView.as_view(), name = 'register'),
        
        ]



