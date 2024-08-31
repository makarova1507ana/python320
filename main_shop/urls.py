from django.urls import path
from main_shop import views
urlpatterns = [
path('', views.index),  # http://127.0.0.1:8000/ маршрут к главной странице
path('news/', views.news),
path('catalog/', views.catalog)
]