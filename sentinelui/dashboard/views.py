import os
from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
from tensorflow import keras
import cv2

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from .models import Camera
import numpy as np


def predict(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        model_path = os.path.abspath('static/assets/people.h5')
        mod = load_model(model_path)
        img = image.load_img(image, target_size=(160, 160))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array /= 255.0  # Scale pixel values to [0, 1]
        predictions = mod.predict(img_array)
        

        return HttpResponse(predictions)
        
        

    return render(request, 'dashboard/predict.html')



def camera_feed(request, pk):
    cam = Camera.objects.get(id=pk)


    context = {
        'cam': cam,
    }

    return render(request, 'dashboard/camera.html', context)



def addCamera(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        feed_links = request.POST.get('feed_links')
        desc = request.POST.get('desc')

        # Create and save the new camera object
        Camera.objects.create(
            name=name,
            feed_links=feed_links,
            desc=desc,
            user = request.user,
        )

        return HttpResponse('Camera added successfully')
    return render(request, 'dashboard/addCamera.html')



def index(request):
    product = Camera.objects.all()
    
    context={'products': product}
    return render(request, 'dashboard/index.html', context)
