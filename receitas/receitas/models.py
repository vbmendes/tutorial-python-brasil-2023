from django.contrib.postgres.fields import ArrayField
from django.db import models


class Receita(models.Model):
    titulo = models.CharField(max_length=255)
    ingredientes = ArrayField(base_field=models.CharField(max_length=255))
    modo_preparo = models.TextField()
