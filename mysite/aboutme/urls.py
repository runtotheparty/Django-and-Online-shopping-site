from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('online_shop', views.online_shop, name='online_shop'),
    path('about_me', views.about_me, name='about_me'),
]