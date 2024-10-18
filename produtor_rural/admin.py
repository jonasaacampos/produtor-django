from django.contrib import admin
from .models import ProdutorRural, Fazenda

# admin.site.register(ProdutorRural)
# admin.site.register(Fazenda)

@admin.register(ProdutorRural)
class ProdutorRuralAdmin(admin.ModelAdmin):
    list_display = ('cpf_cnpj', 'nome')
    search_fields = ('cpf_cnpj', 'nome')
    list_filter = ('nome',)
    ordering = ('nome',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('cpf_cnpj', 'nome')}),
    )

@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    list_display = ('produtor', 'nome', 'cidade', 'estado', 'area_total', 'area_agricultavel', 'area_vegetacao', 'culturas')
    search_fields = ('produtor__nome', 'nome', 'cidade', 'estado', 'culturas')
    list_filter = ('produtor', 'cidade', 'estado')
    ordering = ('produtor', 'nome')

