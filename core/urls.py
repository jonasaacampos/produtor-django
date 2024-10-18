from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Página inicial")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtor_rural/', include('produtor_rural.urls')),
    path('', home, name='home'),  # Adiciona a rota para a URL raiz
]