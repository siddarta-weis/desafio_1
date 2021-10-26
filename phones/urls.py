from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'phones'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:phone_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
]