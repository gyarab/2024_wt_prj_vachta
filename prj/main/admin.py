from django.contrib import admin
from .models import VKosiku, Produkt, Genre, Objednavka

class VKosikuAdmin(admin.ModelAdmin):
    list_display = ['id', 'produkt']

class ObjednavkaAdmin(admin.ModelAdmin):
    list_display = ['id', 'datum']  # pouze existující pole

class ProduktAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'popis', 'obrazek', 'cena', 'barva', 'velikost', 'kategorie')

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(VKosiku, VKosikuAdmin)
admin.site.register(Produkt, ProduktAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Objednavka, ObjednavkaAdmin)