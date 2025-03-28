from django.contrib import admin
from .models import Model, Produkt

class ObuvAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year","produkt"]
    
class ProduktAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]

# Register your models here.
admin.site.register(Model, ObuvAdmin)
admin.site.register(Produkt, ProduktAdmin)