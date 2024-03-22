from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('input/', views.input_sequence, name='input'),
    path('result/', views.result, name='result'),
    path('previous_results/',views.previous_results, name='previous_results'),
]