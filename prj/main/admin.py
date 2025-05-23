from django.contrib import admin
from .models import VKosiku, Produkt, Genre

class ObjednavkaAdmin(admin.ModelAdmin):
    list_display = ["id", "jmeno", "rok","produkt"]
    
class ProduktAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'popis', 'obrazek', 'cena', 'barva', 'velikost', 'kategorie')
    
class GenreAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(VKosiku, ObjednavkaAdmin)
admin.site.register(Produkt, ProduktAdmin)
admin.site.register(Genre, GenreAdmin)