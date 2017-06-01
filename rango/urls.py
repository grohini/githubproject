from django.conf.urls import url
from django.contrib import admin
from rango import views
from django.conf.urls import include
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'aboutus/',views.aboutus,name ='aboutus'),
]
