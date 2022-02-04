from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
import joblib
from .forms import InputForm
import numpy as np
from keras.preprocessing import image


# Create your views here.

def home(request):
    context = {}
    context['form'] = InputForm()
    if (request.method == "POST"):
        print(request.POST)
        
    return render(request,'malaria.html',context)

def result(request):
    data = []
    
    if (request.method == "POST"):
        
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES['file']
    
    model = joblib.load(r'C:\Users\Raj\Desktop\ml-healthcare\ml_health\malaria\malariamodel\model111.h5')
    test_image = image.img_to_array(img)
    test_image = np.expand_dims(test_image, axis = 0)

    predictions = model.predict(test_image)
    context ={}
    if (predictions[0]):
        context['predictions'] = 'Congrats ! You are Healthy'
    else:
        context['predictions'] = 'Sorry,Suffering'   
    
    
    
       
    return render(request,'result.html',context)