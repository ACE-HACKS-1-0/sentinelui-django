from .views import index, camera_feed, addCamera,detect_face
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('cam/<str:pk>', camera_feed, name='camera_feed'),
    #path('predict', predict, name='predict'),
    path('add-camera', addCamera, name='add-camera'),
    path('detect-face/', detect_face, name='detect_face'),

    


]
