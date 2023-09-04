from django.urls import path
from .models import Personagens
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('pers/',views.personagens,name='personagens'),
    path('personagens/',views.personagens,name='personagens'),
    path('tipografia/',views.tipografia,name='tipografia')
]

for i in Personagens.objects.all():
    urlpatterns.append(path('pers/' + i.nome.lower(),views.info,name=i.nome))
    urlpatterns.append(path('personagens/' + i.nome.lower(),views.info,name=i.nome))