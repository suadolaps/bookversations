from django.urls import path

from . import views

app_name = 'bookversations'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'subscribe/', views.subscribe, name='subscribe'),

]

