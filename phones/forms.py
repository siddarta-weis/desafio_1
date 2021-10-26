from django.db import models
from django.forms import ModelForm
from .models import Phone
from django.forms import ModelForm

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'