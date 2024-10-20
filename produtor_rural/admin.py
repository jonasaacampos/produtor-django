from django.contrib import admin
from .models import ProdutorRural, Fazenda
from .forms import FazendaForm

# admin.site.register(ProdutorRural)
# admin.site.register(Fazenda)

@admin.register(ProdutorRural)
class ProdutorRuralAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf_cnpj')
    search_fields = ('cpf_cnpj', 'nome')
    list_filter = ('nome',)
    ordering = ('nome',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('cpf_cnpj', 'nome')}),
    )

@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    form = FazendaForm
    list_display = ('nome', 'produtor', 'cidade', 'estado', 'area_total', 'culturas')
    search_fields = ('produtor__nome', 'nome', 'cidade', 'estado', 'culturas')
    list_filter = ('produtor', 'cidade', 'estado')
    ordering = ('produtor', 'nome')

