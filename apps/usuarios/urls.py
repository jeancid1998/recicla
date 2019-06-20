from django.conf.urls import url, include
from apps.usuarios.views import index,info,RegistroUsuario

from django.urls import include, path

app_name = "index";

urlpatterns = [
url(r'^$', index,name='Menu'),
url(r'^informacion$', info, name='informacion'),
url(r'^registrarse$', RegistroUsuario.as_view(), name='registrarse'),
]