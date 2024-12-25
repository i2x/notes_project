from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.calculator_v1, name='calculator-v1'),
    path('v2/', views.calculator_v2, name='calculator-v2'),
    path('v3/', views.calculator_v3, name='calculator-v3'),
]
