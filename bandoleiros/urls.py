from django.urls import path
from .models import Personagens
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('pers/',views.personagens,name='personagens')
]

for i in Personagens.objects.all():
    urlpatterns.append(path('pers/' + i.nome.lower(),views.info,name=i.nome))