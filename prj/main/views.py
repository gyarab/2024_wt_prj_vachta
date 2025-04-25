from django.shortcuts import render
from main.models import Produkt

def get_homepage(request):
    context = {
        "svatek": "Libor",
        "jmeno": Produkt.objects.all()
     }

    return render(request,"main/base.html", context)