from django.urls import path, include
from product import views

url_patterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
]
