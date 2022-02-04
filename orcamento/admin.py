from re import search
from django.contrib import admin
from orcamento.models import Receita, Despesa

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('descricao', 'valor')
    search_fields = ('descricao', 'valor')
    list_per_page = 30

admin.site.register(Receita, Receitas)

class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data', 'categoria')
    list_display_links = ('descricao', 'valor')
    search_fields = ('descricao', 'valor')
    list_per_page = 30

admin.site.register(Despesa, Despesas)