from django.db.models import Sum, Count
from produtor_rural.models import ProdutorRural, Fazenda

def fetch_dashboard_data():
    produtores = ProdutorRural.objects.all()
    fazendas = Fazenda.objects.all()
    total_fazendas = fazendas.count()
    area_total = fazendas.aggregate(Sum('area_total'))['area_total__sum']
    area_agricultavel = fazendas.aggregate(Sum('area_agricultavel'))['area_agricultavel__sum']
    area_vegetacao = fazendas.aggregate(Sum('area_vegetacao'))['area_vegetacao__sum']
  
    estado_count = fazendas.values('estado').annotate(count=Count('estado'))
    cultura_count = fazendas.values('culturas').annotate(count=Count('culturas'))
    estado_count_queryset = Fazenda.objects.values('estado').annotate(count=Count('estado'))
    estado_count = list(estado_count_queryset)
    
    return {
        'produtores': produtores,
        'fazendas': fazendas,
        'total_fazendas': total_fazendas,
        'area_total': area_total,
        'area_agricultavel': area_agricultavel,
        'area_vegetacao': area_vegetacao,
        'estado_count': estado_count,
        'cultura_count': cultura_count,
    }