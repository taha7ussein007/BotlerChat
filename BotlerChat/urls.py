from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat.views import index


urlpatterns = [
    # url(r'^$', views.reg_redirect, name='reg_redirect'),
    # url(r'^registration/', include('registration.urls')),
    url(r'^$', index),
    url(r'^accounts/login/$', login , name='Login'),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/', admin.site.urls),
]
