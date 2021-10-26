from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Cria a Model e seus atributos.
class Phone(models.Model):
	name = models.CharField(max_length=200, blank=False)
	email = models.EmailField(blank=True)
	phone_number = PhoneNumberField(blank=False)
	address = models.CharField(max_length=200, blank=True)


