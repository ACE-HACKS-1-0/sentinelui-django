from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
def camera_feed(request):
    return render(request, 'dashboard/camera.html')



def index(request):
    return render(request, 'dashboard/index.html')
