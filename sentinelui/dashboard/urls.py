from .views import index, camera_feed, predict
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('cam', camera_feed, name='camera_feed'),
    path('predict', predict, name='predict')

]
