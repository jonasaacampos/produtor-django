from django.urls import path
from .views import dashboard, generate_chart, generate_pie_chart, home, generate_pie_chart_culturas, generate_pie_chart_solo_usage
from .autocomplete import CidadeAutocomplete

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("cidade-autocomplete/", CidadeAutocomplete.as_view(), name="cidade-autocomplete"),
    path("generate_chart/", generate_chart, name="generate_chart"),
    path("generate_pie_chart/", generate_pie_chart, name="generate_pie_chart"),
    path("generate_pie_chart_culturas/", generate_pie_chart_culturas, name="generate_pie_chart_culturas"),
    path("generate_pie_chart_solo_usage/", generate_pie_chart_solo_usage, name="generate_pie_chart_solo_usage"),
    
]
