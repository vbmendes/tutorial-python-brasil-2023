from django.shortcuts import render
from rest_framework import viewsets
from .models import Receita
from .serializers import ReceitaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
