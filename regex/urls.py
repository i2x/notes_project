from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='regex_index'),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.article_by_year, name='article_by_year'),
    re_path(r'^check-email/(?P<email>.+)/$', views.check_email, name='check_email'),
]
