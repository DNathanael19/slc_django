from django.db import models


# Create your models here.
class Lista(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"

class Iten(models.Model):
    item = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name="departures")

    def __str__(self):
        return f"{self.id}: {self.item}"
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    flights = models.ManyToManyField(Iten, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first}"