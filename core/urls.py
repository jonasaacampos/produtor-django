from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from produtor_rural import views

def home(request):
    return HttpResponse("Página inicial")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtor_rural/', include('produtor_rural.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),  # Adiciona a rota para a URL 'dashboard/'
    path('', home, name='home'),  # Adiciona a rota para a URL raiz
]