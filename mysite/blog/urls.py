from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    path(r'^activate/<uidb64>/<token>/$',
        views.activate, name='activate'),
]