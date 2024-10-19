from django.urls import path
from .views import dashboard, generate_chart
from .autocomplete import CidadeAutocomplete

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("cidade-autocomplete/", CidadeAutocomplete.as_view(), name="cidade-autocomplete"),
    path("generate_chart/", generate_chart, name="generate_chart"),
]
