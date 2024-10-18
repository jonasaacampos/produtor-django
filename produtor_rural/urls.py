from django.urls import path
from .views import dashboard
from .autocomplete import CidadeAutocomplete

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('cidade-autocomplete/', CidadeAutocomplete.as_view(), name='cidade-autocomplete'),
]
