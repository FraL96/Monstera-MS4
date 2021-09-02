from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_collect, name='email_collect'),
]