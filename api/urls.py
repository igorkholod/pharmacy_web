from django.urls import path
from . import views

urlpatterns = [
    path('drug/<int:id>/', views.DrugView.as_view()),
    path('pharmacy/<int:id>/', views.PharmacyView.as_view()),
    path('search/<str:search>/', views.DrugSearchView.as_view()),
    path('search_pharmacy/<int:id>/', views.PharmacySearchView.as_view()),
]