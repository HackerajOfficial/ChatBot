from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('getResponse', views.getResponse, name='getResponse'),
    path('train', views.train_through_document, name='train'),
]