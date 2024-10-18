# produtor_rural/views.py

from django.shortcuts import render
from .models import ProdutorRural, Fazenda
from django.db.models import Count, Sum

def dashboard(request):
    produtores = ProdutorRural.objects.all()
    fazendas = Fazenda.objects.all()
    total_fazendas = fazendas.count()
    area_total = fazendas.aggregate(Sum('area_total'))['area_total__sum']
    area_agricultavel = fazendas.aggregate(Sum('area_agricultavel'))['area_agricultavel__sum']
    area_vegetacao = fazendas.aggregate(Sum('area_vegetacao'))['area_vegetacao__sum']
    
    estado_count = fazendas.values('estado').annotate(count=Count('estado'))
    cultura_count = fazendas.values('culturas').annotate(count=Count('culturas'))

    return render(request, 'produtor/dashboard.html', {  # Corrigido o caminho do template
        'produtores': produtores,
        'fazendas': fazendas,
        'total_fazendas': total_fazendas,
        'area_total': area_total,
        'area_agricultavel': area_agricultavel,
        'area_vegetacao': area_vegetacao,
        'estado_count': estado_count,
        'cultura_count': cultura_count,
    })


def grafico_uso_solo(request):
    # Supondo que você tenha um único objeto no modelo
    uso_solo = Fazenda.objects.first()
    
    context = {
        'area_agricultavel': uso_solo.area_agricultavel,
        'area_vegetacao': uso_solo.area_vegetacao,
    }
    
    return render(request, 'seu_template.html', context)
