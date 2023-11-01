from rest_framework import serializers

from .models import Receita


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ("titulo", "ingredientes", "modo_preparo")
