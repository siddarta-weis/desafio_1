from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Phone
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import redirect
from django.contrib import messages
import django_filters
from .filters import PhoneFilter
from .forms import PhoneForm

def index(request):
	phones_list = Phone.objects.all().order_by('name') # Pega todos os objetos de Phone
	phones_filter = PhoneFilter(request.GET, queryset=phones_list) # Filtra os objetos pelo nome que foi escrito
	if phones_list:
		return render(request, 'phones/index.html', {'filter': phones_filter, 'phones_list': phones_list})
	else:
		return render(request, 'phones/index.html', {'filter': "", 'phones_list': ""})

	

def detail(request, phone_id):
	item = get_object_or_404(Phone, pk=phone_id)
	if request.method == 'POST': #verifica o método utilizado
		form = PhoneForm(request.POST or None, instance=item)
		if 'edit_button' in request.POST: # se o botão utilizado foi o de edição
			if form.is_valid(): # verifica se o formulário é válido
					form.save()
					messages.success(request, 'Contato editado com sucesso!')
					return redirect('phones:index')

		if 'delete_button' in request.POST:
				item = Phone.objects.get(pk=phone_id)
				item.delete()
				messages.warning(request, 'Contato excluído com sucesso!')
				return redirect('phones:index')
	else:
		form = PhoneForm(instance=item)
	return render(request, 'phones/detail.html', {'form': form})


def add(request):
	if request.method == 'POST':
		form = PhoneForm(request.POST)
		if form.is_valid():
			form.save()  
			messages.success(request, 'Contato criado com sucesso!')
			return redirect('phones:index')
	else:
		form = PhoneForm()
	return render(request, 'phones/add.html', {'form': form})
'''
def search(request):
	phones_list = Phone.objects.all()
	phones_filter = PhoneFilter(request.GET, queryset=phones_list)
	return render(request, 'phones/search.html', {'filter': phones_filter})
'''