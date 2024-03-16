import os
from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
from tensorflow import keras
import cv2

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

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



def camera_feed(request):
    return render(request, 'dashboard/camera.html')



def index(request):
    return render(request, 'dashboard/index.html')
