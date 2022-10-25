"""Helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path as path

from . import views, testdb, search, search2

urlpatterns = [
    path(r'^runoob$', views.runoob),
    path(r'^testdb/$', testdb.testdb),
    path(r'^search-form/$', search.search_form),
    path(r'^search/$', search.search),
    path(r'^search-post/$', search2.search_post),
]
