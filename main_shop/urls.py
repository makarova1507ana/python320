from django.urls import path
from main_shop import views

urlpatterns = [
path('', views.index),  # http://127.0.0.1:8000/ маршрут к главной странице
path('news/', views.news, name="news"),# http://127.0.0.1:8000/news/
path('catalog/', views.catalog, name="catalog"),
path('item/<int:product_id>', views.product, name="product_url"),
]