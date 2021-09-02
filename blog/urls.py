from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='blog'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
]