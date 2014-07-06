from django.conf.urls import patterns, url
from DiscussGroup import views


urlpatterns = patterns('',
        url(r'^$', views.user_login, name='log_in'),

        url(r'^Login/$', views.IndexStudent, name='IndexStudent'))
