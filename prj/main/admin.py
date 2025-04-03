from django.contrib import admin
from .models import VKosiku, Produkt

class ObjednavkaAdmin(admin.ModelAdmin):
    list_display = ["id", "jmeno", "rok","produkt"]
    
class ProduktAdmin(admin.ModelAdmin):
    list_display = ["id", "jmeno", "obrazek", "cena", "barva", "velikost", "recenze"]

# Register your models here.
admin.site.register(VKosiku, ObjednavkaAdmin)
admin.site.register(Produkt, ProduktAdmin)