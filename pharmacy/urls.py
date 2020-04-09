from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('search', views.search_result, name='search_result'),
    path('pharmacy_result', views.pharmacy_result, name='pharmacy_result'),
    path('drug', views.drug_info, name='drug_info'),
    path('about', views.about, name='about'),
]
