from django.conf.urls import  url
from . import views
from django.contrib.auth.views import login

app_name = 'registration'

urlpatterns =[
    # url(r'^$', views.index, name='index'),
    # url(r'^registration/registered$', views.registered, name='registered'),
    url(r'^accounts/login/$', login , name='Login'),


]