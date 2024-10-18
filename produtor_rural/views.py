# produtor/views.py

from django.shortcuts import render
from .models import ProdutorRural, Fazenda

def dashboard(request):
    produtores = ProdutorRural.objects.all()
    total_fazendas = sum(produtor.fazendas.count() for produtor in produtores)
    area_total = sum(fazenda.area_total for produtor in produtores for fazenda in produtor.fazendas.all())
    
    estado_count = {}
    cultura_count = {}
    uso_solo = {"Agricultável": 0, "Vegetação": 0}

    for produtor in produtores:
        for fazenda in produtor.fazendas.all():
            # Contagem por estado
            estado_count[fazenda.estado] = estado_count.get(fazenda.estado, 0) + 1
            
            # Contagem por cultura
            for cultura in fazenda.culturas.split(", "):
                cultura_count[cultura] = cultura_count.get(cultura, 0) + 1
            
            # Soma de áreas por uso do solo
            uso_solo["Agricultável"] += fazenda.area_agricultavel
            uso_solo["Vegetação"] += fazenda.area_vegetacao

    context = {
        'total_fazendas': total_fazendas,
        'area_total': area_total,
        'estado_count': estado_count,
        'cultura_count': cultura_count,
        'uso_solo': uso_solo,
    }
    
    return render(request, 'produtor/dashboard.html', context)
