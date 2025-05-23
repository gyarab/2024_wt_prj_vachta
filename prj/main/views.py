from django.shortcuts import redirect, get_object_or_404
from faker import Faker
from django.shortcuts import render
from main.models import Produkt, Genre, VKosiku

def get_homepage(request):
    produkt = Produkt.objects.all().order_by("jmeno")

    search = request.GET.get("search")
    if search:
        produkt = produkt.filter(jmeno__icontains=search) | Produkt.objects.filter(popis__icontains=search)

    genre = request.GET.get("genre")
    if genre:
        produkt = produkt.filter(genre__jmeno=genre)

    kategorie = request.GET.get("kategorie")
    if kategorie:
        produkt = produkt.filter(kategorie=kategorie)

    produkt = produkt[:10]

    context = {
        "produkty": produkt,
        "genres": Genre.objects.all().order_by("jmeno")[:10],
        "kategorie": kategorie,
    }
    return render(request, "main/homepage.html", context)
    
def produkty_list(request):
    produkt = Produkt.objects.first()
    if produkt:
        return redirect('produkt_detail', id=produkt.id)
    else:
        return redirect('homepage')
    
def get_produkty(request, id):
    produkt = Produkt.objects.get(id=id)
    objednano = False

    if request.method == "POST":
        VKosiku.objects.create(jmeno="Objednávka", produkt=produkt)
        objednano = True

    context = {
        "produkt": produkt,
        "objednano": objednano,
    }
    return render(request, "main/produkt.html", context)
    
def get_obednavky(request):
    objednavky = VKosiku.objects.all().order_by('-id')
    context = {"objednavky": objednavky}
    return render(request, "main/objednavka.html", context)

def zrusit_objednavku(request, objednavka_id):
    if request.method == "POST":
        try:
            objednavka = VKosiku.objects.get(id=objednavka_id)
            objednavka.delete()
        except VKosiku.DoesNotExist:
            pass  # Objednávka už neexistuje, ignoruj
    return redirect('obednavky')

def get_vkosiku(request):
    return render(request, 'main/vkosiku.html')