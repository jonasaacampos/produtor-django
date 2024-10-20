from django.urls import path
from .views import (
    dashboard,
    generate_bar_chart_farms_per_state,
    generate_pie_chart_farms_per_state,
    home,
    generate_pie_chart_culturas,
    generate_pie_chart_solo_usage,
    generate_bar_chart_solo_usage,
    generate_stacked_bar_chart_culturas,
    generate_bar_horizontal_chart_solo_usage
)
from .autocomplete import CidadeAutocomplete

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path(
        "cidade-autocomplete/", CidadeAutocomplete.as_view(), name="cidade-autocomplete"
    ),
    path(
        "generate_bar_chart_farms_per_state/",
        generate_bar_chart_farms_per_state,
        name="generate_bar_chart_farms_per_state",
    ),
    path(
        "generate_pie_chart_farms_per_state/",
        generate_pie_chart_farms_per_state,
        name="generate_pie_chart_farms_per_state",
    ),
    path(
        "generate_pie_chart_culturas/",
        generate_pie_chart_culturas,
        name="generate_pie_chart_culturas",
    ),
    path(
        "generate_pie_chart_solo_usage/",
        generate_pie_chart_solo_usage,
        name="generate_pie_chart_solo_usage",
    ),
    path(
        "generate-bar-chart/",
        generate_bar_chart_solo_usage,
        name="generate_bar_chart_solo_usage",
    ),
    path(
        "generate-stacked-bar-chart/",
        generate_stacked_bar_chart_culturas,
        name="generate_stacked_bar_chart_culturas",
    ),
    path(
        "generate_bar_horizontal_chart_solo_usage/",
        generate_bar_horizontal_chart_solo_usage,
        name="generate_bar_horizontal_chart_solo_usage",
    ),
]
