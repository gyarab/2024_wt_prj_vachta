from django.shortcuts import render
from faker import Faker
from django.shortcuts import render
from main.models import Produkt, Genre

def get_homepage(request):
    produkt = Produkt.objects.all().order_by("jmeno")[:10]
    
    search = request.GET.get("search")
    if search:
        produkt = produkt.filter(jmeno__icontains=search) | produkt.filter(popis__icontains=search)
    
    genre = request.GET.get("genre")
    if genre:
        produkt = produkt.filter(genre__jmeno=genre)
    
    context = {
        "produkty": produkt,
        "genres": Genre.objects.all().order_by("jmeno")[:10]
     }
    return render(
        request, "main/homepage.html", context
    )
    
def get_produkty(request, id):
    print(id)
    produkt = Produkt.objects.get(id=id)
    context = {
        "name": Faker().name(),
        "email": Faker().email(),
        "phone": Faker().phone_number(),
   }
    return render(
        request, "main/random.html", context
    )
    
def get_obednavky(request):
    return render(request, 'main/obednavky.html')

def get_vkosiku(request):
    return render(request, 'main/vkosiku.html')