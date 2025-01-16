from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    path('', views.index, name='regex_index'),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.article_by_year, name='article_by_year'),
    re_path(r'^profile/(?P<username>[a-zA-Z0-9_]+)/$', views.profile, name='profile'),
]
