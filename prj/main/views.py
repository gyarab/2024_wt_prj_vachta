from django.shortcuts import render
from main.models import Produkt

def get_homepage(request):
    produkt = Produkt.objects.all().order_by("jmeno")[:10]
    
    context = {
        "svatek": "Libor",
        "jmeno": Produkt.objects.all().order_by("jmeno")[:10]
     }

    if request.GET.get("search"):
        print("SEARCH", request.GET.get("search"))
        produkt = Produkt.filter(title_icontains=request.GET.get("search")).order_by("jmeno")[:10]
    
    return render(
        request, "main/base.html", context
    )