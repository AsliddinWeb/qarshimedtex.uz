from django.urls import path
from .views import news_detail, all_news, category_news, news_search

urlpatterns = [
    path('', all_news, name='all_news'),
    path('category/<int:category_pk>/', category_news, name='category_news'),
    path('<int:pk>/', news_detail, name='news_detail'),
    path('search/', news_search, name='news_search'),
]
