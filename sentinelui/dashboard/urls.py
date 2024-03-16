from .views import index, camera_feed
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('cam', camera_feed, name='camera_feed')

]
