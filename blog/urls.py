from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='blog'),
    path('<slug:slug>/', views.article_detail, name='article_detail')
]