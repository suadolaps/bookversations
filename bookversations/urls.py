from django.urls import path, re_path
from django.conf.urls import url

from . import views

app_name = 'bookversations'
urlpatterns = [
    re_path(r'^.*', views.index, name='index'),
    re_path(r'^subscribe/', views.newsletter_signup, name='subscribe'),
    re_path(r'^failure/', views.failure_retry, name='failure'),

]

