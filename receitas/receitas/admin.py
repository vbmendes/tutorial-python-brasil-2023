from django.contrib import admin
from .models import Receita


class ReceitaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Receita, ReceitaAdmin)
