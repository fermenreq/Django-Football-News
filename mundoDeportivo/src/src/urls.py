"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mundoDeportivo import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

#Para usar template view importamos:
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.UserFormView, name="index"),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^noticias/(?P<pk>\d+)/$',noticias, name="noticias"),
    url(r'^equipos/$',equipo, name="equipos"),
    #url(r'^about/$',about, name="about"),
    
    #---------------Usando template view--------------------------
    #url(r'^equipos/$',TemplateView.as_view(template_name='equipos.html')),
    url(r'^about/$',TemplateView.as_view(template_name='about.html')),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    