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
import os
import requests

# Use o backend 'Agg' para evitar problemas com GUI
matplotlib.use("Agg")


def dashboard(request):
    data = fetch_dashboard_data()
    return render(request, "produtor/dashboard.html", data)


def home(request):
    data = fetch_dashboard_data()
    return render(request, "home.html", data)


############################################################################################################
#                                              Gráficos                                                    #
############################################################################################################

# Fazendas por Estado


def generate_bar_chart_farms_per_state(ax=None, save_path=None):
    estado_count = get_estado_count()
    df = pd.DataFrame(estado_count)

    # Gerar cores aleatórias para cada barra
    colors = ["#%06X" % random.randint(0, 0xFFFFFF) for _ in range(len(df))]

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    ax.bar(df["estado"], df["count"], color=colors)
    ax.set_title("Gráfico por Estado")
    ax.set_xlabel("Estado")
    ax.set_ylabel("Count")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        plt.close(fig)
    else:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close(fig)
        return HttpResponse(buffer, content_type="image/png")


def generate_pie_chart_farms_per_state(ax=None, save_path=None):
    estado_count = get_estado_count()
    df = pd.DataFrame(estado_count)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    ax.pie(df["count"], labels=df["estado"], autopct="%1.1f%%")
    ax.set_title("Gráfico por Estado")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        plt.close(fig)
    else:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close(fig)
        return HttpResponse(buffer, content_type="image/png")

def generate_stacked_bar_chart_culturas(ax=None, save_path=None):
    cultura_count = get_cultura_count()

    if not cultura_count:
        return HttpResponse("No data available", content_type="text/plain")

    if not isinstance(cultura_count, list) or not all(
        isinstance(item, dict) for item in cultura_count
    ):
        return HttpResponse("Invalid data format", content_type="text/plain")
    if not all("culturas" in item and "count" in item for item in cultura_count):
        return HttpResponse("Invalid data format", content_type="text/plain")

    df = pd.DataFrame(cultura_count)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    df.set_index("culturas").T.plot(kind="bar", stacked=True, ax=ax)
    ax.set_title("Gráfico de Culturas Cultivadas")
    ax.set_xlabel("Culturas")
    ax.set_ylabel("Contagem")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        plt.close(fig)
    else:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close(fig)
        return HttpResponse(buffer, content_type="image/png")

def generate_pie_chart_culturas(ax=None, save_path=None):
    cultura_count = get_cultura_count()

    if not cultura_count:
        return HttpResponse("No data available", content_type="text/plain")

    if not isinstance(cultura_count, list) or not all(
        isinstance(item, dict) for item in cultura_count
    ):
        return HttpResponse("Invalid data format", content_type="text/plain")
    if not all("culturas" in item and "count" in item for item in cultura_count):
        return HttpResponse("Invalid data format", content_type="text/plain")

    df = pd.DataFrame(cultura_count)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    ax.pie(df["count"], labels=df["culturas"], autopct="%1.1f%%")
    ax.set_title("Gráfico de Culturas Cultivadas")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        plt.close(fig)
    else:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close(fig)
        return HttpResponse(buffer, content_type="image/png")


# Gráfico de Uso do Solo


def generate_pie_chart_solo_usage(ax=None, save_path=None):
    solo_agricultavel = get_solo_agricultavel_count()
    solo_preservado = get_solo_preservado_count()

    # Calcular as áreas totais em hectares
    total_agricultavel = sum(item["area_agricultavel"] for item in solo_agricultavel)
    total_preservado = sum(item["area_vegetacao"] for item in solo_preservado)

    # Rótulos e tamanhos para o gráfico de pizza
    labels = ["Área Agricultável", "Área Preservada"]
    sizes = [total_agricultavel, total_preservado]

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["#FF6384", "#36A2EB"])
    ax.set_title("Comparação de Uso do Solo em Hectares")
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        plt.close(fig)
    else:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close(fig)
        return HttpResponse(buffer, content_type="image/png")

def generate_bar_horizontal_chart_solo_usage(ax=None, save_path=None):
    solo_agricultavel = get_solo_agricultavel_count()
    solo_preservado = get_solo_preservado_count()

    # Calcular as áreas totais em hectares
    total_agricultavel = sum(item["area_agricultavel"] for item in solo_agricultavel)
    total_preservado = sum(item["area_vegetacao"] for item in solo_preservado)

    # Rótulos e tamanhos para o gráfico de barras
    labels = ["Área Agricultável", "Área Preservada"]
    sizes = [total_agricultavel, total_preservado]

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    ax.barh(labels, sizes, color=["#FF6384", "#36A2EB"])
    ax.set_title("Comparação de Uso do Solo em Hectares")
    ax.set_xlabel("Hectares")

    # Girar as labels
    ax.set_yticklabels(labels, rotation=45)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        plt.close(fig)
    else:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close(fig)
        return HttpResponse(buffer, content_type="image/png")

def generate_bar_chart_solo_usage(ax=None, save_path=None):
    solo_agricultavel = get_solo_agricultavel_count()
    solo_preservado = get_solo_preservado_count()

    # Calcular as áreas totais em hectares
    total_agricultavel = sum(item["area_agricultavel"] for item in solo_agricultavel)
    total_preservado = sum(item["area_vegetacao"] for item in solo_preservado)

    # Rótulos e tamanhos para o gráfico de barras
    labels = ["Área Agricultável", "Área Preservada"]
    sizes = [total_agricultavel, total_preservado]

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    ax.bar(labels, sizes, color=["#FF6384", "#36A2EB"])
    ax.set_title("Comparação de Uso do Solo em Hectares")
    ax.set_ylabel("Hectares")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        plt.close(fig)
    else:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close(fig)
        return HttpResponse(buffer, content_type="image/png")


############################################################################################################
#                                           Funções auxiliares                                             #
############################################################################################################


def get_estado_count():
    queryset = (
        Fazenda.objects.values("estado")
        .annotate(count=Count("estado"))
        .order_by("estado")
    )
    return list(queryset)


def get_cultura_count():
    queryset = (
        Fazenda.objects.values("culturas")
        .annotate(count=Count("culturas"))
        .order_by("culturas")
    )
    return list(queryset)


def get_solo_agricultavel_count():
    queryset = (
        Fazenda.objects.values("area_agricultavel")
        .annotate(count=Count("area_agricultavel"))
        .order_by("area_agricultavel")
    )
    return list(queryset)


def get_solo_preservado_count():
    queryset = (
        Fazenda.objects.values("area_vegetacao")
        .annotate(count=Count("area_vegetacao"))
        .order_by("area_vegetacao")
    )
    return list(queryset)


############################################################################################################
#                                     Gerar e salvar todos os gráficos                                     #
############################################################################################################
def save_plot_to_file(plot_func, save_path):
    fig, ax = plt.subplots()
    plot_func(ax=ax, save_path=save_path)
    plt.close(fig)

def generate_and_save_all_images():
    from time import sleep


    image_paths = [
        (generate_pie_chart_solo_usage, 'static/img/charts/pie_chart_solo_usage.png'),
        (generate_bar_horizontal_chart_solo_usage, 'static/img/charts/bar_horizontal_chart_solo_usage.png'),
        (generate_bar_chart_solo_usage, 'static/img/charts/bar_chart_solo_usage.png'),
        (generate_pie_chart_farms_per_state, 'static/img/charts/pie_chart_farms_per_state.png'),
        (generate_bar_chart_farms_per_state, 'static/img/charts/bar_chart_farms_per_state.png'),
        (generate_pie_chart_culturas, 'static/img/charts/pie_chart_culturas.png'),
        (generate_stacked_bar_chart_culturas, 'static/img/charts/stacked_bar_chart_culturas.png'),

    ]

    for plot_func, save_path in image_paths:
        save_plot_to_file(plot_func, save_path)