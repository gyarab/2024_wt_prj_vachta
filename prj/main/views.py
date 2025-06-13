from django.shortcuts import redirect, get_object_or_404, render
from main.models import Produkt, Genre, VKosiku, Objednavka

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
        "kosik_pocet": VKosiku.objects.count(),
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
    pridano = False
    if request.method == "POST":
        VKosiku.objects.create(produkt=produkt)
        pridano = True
    context = {
        "produkt": produkt,
        "pridano": pridano,
        "kosik_pocet": VKosiku.objects.count(),
    }
    return render(request, "main/produkt.html", context)

def get_vkosiku(request):
    produkty_v_kosiku = VKosiku.objects.all()
    context = {
        "produkty_v_kosiku": produkty_v_kosiku,
        "kosik_pocet": VKosiku.objects.count(),
    }
    return render(request, 'main/vkosiku.html', context)

def vytvor_objednavku(request):
    if request.method == "POST":
        produkty_v_kosiku = VKosiku.objects.all()
        if produkty_v_kosiku:
            objednavka = Objednavka.objects.create()
            for polozka in produkty_v_kosiku:
                objednavka.produkty.add(polozka.produkt)
            produkty_v_kosiku.delete()
        return redirect('obednavky')
    return redirect('vkosiku')

def get_obednavky(request):
    objednavky = Objednavka.objects.all().order_by('-id')
    context = {
        "objednavky": objednavky,
        "kosik_pocet": VKosiku.objects.count(),
    }
    return render(request, "main/objednavka.html", context)

def zrusit_objednavku(request, objednavka_id):
    if request.method == "POST":
        try:
            objednavka = Objednavka.objects.get(id=objednavka_id)
            objednavka.delete()
        except Objednavka.DoesNotExist:
            pass
    return redirect('obednavky')