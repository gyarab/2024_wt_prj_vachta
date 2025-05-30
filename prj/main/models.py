from django.db import models

class VKosiku(models.Model):
    produkt = models.ForeignKey('Produkt', on_delete=models.CASCADE)
    jmeno = models.CharField(max_length=300, default="Košík", blank=True)

class Objednavka(models.Model):
    produkty = models.ManyToManyField('Produkt')
    datum = models.DateTimeField(auto_now_add=True)

    @property
    def cena_celkem(self):
        return sum(produkt.cena for produkt in self.produkty.all())


class Produkt(models.Model):
    KATEGORIE_VOLBY = [
        ('detske', 'Dětské'),
        ('damske', 'Dámské'),
        ('panske', 'Pánské'),
    ]
    jmeno = models.CharField(max_length=300)
    popis = models.TextField(blank=True, default="")
    obrazek = models.ImageField(upload_to='produkty/', blank=True, null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    barva = models.CharField(max_length=100, blank=True)
    velikost = models.CharField(max_length=50, blank=True)
    kategorie = models.CharField(max_length=10, choices=KATEGORIE_VOLBY, default='detske')

    def __str__(self):
        return f"Produkt {self.jmeno} {self.popis} {self.obrazek} {self.cena} {self.barva} {self.velikost}"
    
class Genre(models.Model):
    jmeno = models.CharField(max_length=300)

    def __str__(self):
        return self.name