from django.shortcuts import render
from .models import ProdutorRural, Fazenda
from django.db.models import Count, Sum
from produtor_rural.utils.data_fetcher import fetch_dashboard_data

# para gráficos com pandas
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from django.http import HttpResponse
import io
import base64
import random

# Use o backend 'Agg' para evitar problemas com GUI
matplotlib.use('Agg')


def dashboard(request):
    data = fetch_dashboard_data()
    return render(request, 'produtor/dashboard.html', data)

def home(request):
    data = fetch_dashboard_data()
    return render(request, 'home.html', data)

def generate_chart(request):
    estado_count = get_estado_count()
    df = pd.DataFrame(estado_count)

    # Gerar cores aleatórias para cada barra
    colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(len(df))]

    plt.figure(figsize=(10, 5))
    plt.bar(df['estado'], df['count'], color=colors)
    plt.title('Gráfico por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Count')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')

def generate_pie_chart(request):
    estado_count = get_estado_count()
    df = pd.DataFrame(estado_count)

    plt.figure(figsize=(10, 5))
    plt.pie(df['count'], labels=df['estado'], autopct='%1.1f%%')
    plt.title('Gráfico por Estado')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')


def generate_pie_chart_culturas(request):
    cultura_count = get_cultura_count()
    
    # print("Tipo de cultura_count:", type(cultura_count))
    # print("Formato de cultura_count:", cultura_count)
    
    if not cultura_count:
        return HttpResponse("No data available", content_type='text/plain')

    if not isinstance(cultura_count, list) or not all(isinstance(item, dict) for item in cultura_count):
        return HttpResponse("Invalid data format", content_type='text/plain')
    if not all('culturas' in item and 'count' in item for item in cultura_count):
        return HttpResponse("Invalid data format", content_type='text/plain')

    df = pd.DataFrame(cultura_count)

    plt.figure(figsize=(10, 5))
    plt.pie(df['count'], labels=df['culturas'], autopct='%1.1f%%')
    plt.title('Gráfico de Culturas Cultivadas')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()  # Fechar a figura para liberar memória
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')


def generate_pie_chart_solo_usage(request):
    solo_usage = get_solo_usage_count
    
    df = pd.DataFrame(solo_usage)

    plt.figure(figsize=(10, 5))
    plt.pie(df['count'], labels=df['Tipo Solo'], autopct='%1.1f%%')
    plt.title('Gráfico de Uso do Solo')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close() 
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')



def get_estado_count():
    queryset = Fazenda.objects.values('estado').annotate(count=Count('estado')).order_by('estado')
    return list(queryset)

def get_cultura_count():
    queryset = Fazenda.objects.values('culturas').annotate(count=Count('culturas')).order_by('culturas')
    return list(queryset)

def get_solo_usage_count():
    queryset = Fazenda.objects.values('uso_solo').annotate(count=Count('uso_solo')).order_by('uso_solo')
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
  
#     return render(request, 'produtor/dashboard.html', {  
#         'produtores': produtores,
#         'fazendas': fazendas,
#         'total_fazendas': total_fazendas,
#         'area_total': area_total,
#         'area_agricultavel': area_agricultavel,
#         'area_vegetacao': area_vegetacao,
#         'estado_count': estado_count,
#         'cultura_count': cultura_count,
#     })