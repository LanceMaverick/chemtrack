from django.contrib import admin

from .models import Reagent, LiquidEntry, SolidEntry

admin.site.register(Reagent)
admin.site.register(LiquidEntry)
admin.site.register(SolidEntry)
