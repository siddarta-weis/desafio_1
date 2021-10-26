from .models import Phone
import django_filters

class PhoneFilter(django_filters.FilterSet):
	#pesquisar utilizando apenas parte do nome
	name = django_filters.CharFilter(lookup_expr='icontains') 

	class Meta:
		model = Phone
		fields = ['name']

	

