from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^article/(\d+)/(\d+)$', views.view_troc),
    url(r'^register/$', views.register, name='register'),
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^compte/$', views.compte, name='compte'),
    url(r'^troc_search/$', views.troc_search, name='troc_search'),
    url(r'^admin/', include(admin.site.urls)),
]
