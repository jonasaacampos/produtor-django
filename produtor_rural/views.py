from django.shortcuts import render
from .models import ProdutorRural, Fazenda
from django.db.models import Count, Sum

# para gráficos com pandas
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from django.http import HttpResponse
import io
import base64

# Use o backend 'Agg' para evitar problemas com GUI
matplotlib.use('Agg')

def dashboard(request):
    estado_count = get_estado_count()
    return render(request, 'produtor/dashboard.html', {'estado_count': estado_count})

def generate_chart(request):
    estado_count = get_estado_count()
    df = pd.DataFrame(estado_count)

    plt.figure(figsize=(10, 5))
    plt.bar(df['estado'], df['count'])
    plt.title('Gráfico por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Count')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')


def get_estado_count():
    queryset = Fazenda.objects.values('estado').annotate(count=Count('estado')).order_by('estado')
    return list(queryset)


# def dashboard(request):
#     produtores = ProdutorRural.objects.all()
#     fazendas = Fazenda.objects.all()
#     total_fazendas = fazendas.count()
#     area_total = fazendas.aggregate(Sum('area_total'))['area_total__sum']
#     area_agricultavel = fazendas.aggregate(Sum('area_agricultavel'))['area_agricultavel__sum']
#     area_vegetacao = fazendas.aggregate(Sum('area_vegetacao'))['area_vegetacao__sum']
    
#     estado_count = fazendas.values('estado').annotate(count=Count('estado'))
#     cultura_count = fazendas.values('culturas').annotate(count=Count('culturas'))

#      # QuerySet para contagem de estados
#     estado_count_queryset = Fazenda.objects.values('estado').annotate(count=Count('estado'))

#     # Convertendo QuerySet para lista de dicionários
#     estado_count = list(estado_count_queryset)

#     context = {

#         'estado_count': estado_count,
#         'tipo_estado_count': type(estado_count).__name__, 
#     }

    
#     return render(request, 'produtor/dashboard.html', {  # Corrigido o caminho do template
#         'produtores': produtores,
#         'fazendas': fazendas,
#         'total_fazendas': total_fazendas,
#         'area_total': area_total,
#         'area_agricultavel': area_agricultavel,
#         'area_vegetacao': area_vegetacao,
#         'estado_count': estado_count,
#         'cultura_count': cultura_count,
#     })


# def grafico_uso_solo(request):
#     # Supondo que você tenha um único objeto no modelo
#     uso_solo = Fazenda.objects.first()
    
#     context = {
#         'area_agricultavel': uso_solo.area_agricultavel,
#         'area_vegetacao': uso_solo.area_vegetacao,
#     }
    
#     return render(request, 'seu_template.html', context)
