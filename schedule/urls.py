from django.conf.urls import patterns, include, url
from schedule import views

urlpatterns = patterns('',
    url(r'^teacher/$', views.teacher, name='teacher'),
)