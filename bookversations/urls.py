from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'bookversations'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^subscribe/$', views.newsletter_signup, name='subscribe'),
    url(r'^failure/$', views.failure_retry, name='failure'),

]

