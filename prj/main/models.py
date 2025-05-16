from django.db import models

class VKosiku(models.Model):
    jmeno = models.CharField(max_length=300)
    rok = models.IntegerField(blank=True, null=True)
    popis = models.TextField(blank=True, default="")
    produkt = models.ForeignKey(
        "Produkt", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"VKosiku {self.jmeno} {self.rok} {self.popis} {self.produkt}"


class Produkt(models.Model):
    jmeno = models.CharField(max_length=300)
    popis = models.TextField(blank=True, default="")
    obrazek = models.ImageField(
        upload_to='produkty/', blank=True, null=True
    )
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    barva = models.CharField(max_length=100, blank=True)
    velikost = models.CharField(max_length=50, blank=True)
    recenze = models.TextField(blank=True, default="")

    def __str__(self):
        return f"Produkt {self.jmeno} {self.popis} {self.obrazek} {self.cena} {self.barva} {self.velikost} {self.recenze}"
    
class Genre(models.Model):
    jmeno = models.CharField(max_length=300)

    def __str__(self):
        return self.name