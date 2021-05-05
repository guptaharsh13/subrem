from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('streamingservices', views.streamingServices, name='streamingServices'),
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('cloudstorage', views.cloudStorage, name='cloudStorage'),
]