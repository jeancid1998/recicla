from django.conf.urls import url, include
from apps.recicladores.views import index,videos,SolicitaAyudaa,recicla1,recicla2,recicla3,recicla4,recicla5,recicla6,recicla7,recicla8

from django.urls import include, path

app_name = "recicladores";

urlpatterns = [
url(r'^$', index,name='Menu'),
url(r'^videos$', videos,name='Videos'),
url(r'^ayuda$', SolicitaAyudaa,name='chat'),
url(r'^punto-reciclaje1$', recicla1, name='punto1'),
url(r'^punto-reciclaje2$', recicla2, name='punto2'),
url(r'^punto-reciclaje3$', recicla3, name='punto3'),
url(r'^punto-reciclaje4$', recicla4, name='punto4'),
url(r'^punto-reciclaje5$', recicla5, name='punto5'),
url(r'^punto-reciclaje6$', recicla6, name='punto6'),
url(r'^punto-reciclaje7$', recicla7, name='punto7'),
url(r'^punto-reciclaje8$', recicla8, name='punto8'),
]