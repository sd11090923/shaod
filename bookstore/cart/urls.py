"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import cart_add,cart_count,cart_show,cart_del,cart_update
urlpatterns = [
       url(r'^add/$',cart_add,name='cart_add'),
       url(r'^count/$',cart_count,name='cart_count'),
       url(r'^$',cart_show,name='show'),
       url(r'^del/$',cart_del,name='delete'),
       url(r'^update/$',cart_update,name='update')

]
