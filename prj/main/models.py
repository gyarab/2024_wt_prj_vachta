from django.db import models
class Model(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, default="")
    produkt = models.ForeignKey("Produkt", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Model <{self.id}> {self.name}"

class Produkt(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)
    birth_year = models.IntegerField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    
    def __str__(self):
        return f"Produkt <{self.id}> {self.name}"
