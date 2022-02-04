from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
import joblib
from .forms import InputForm
import pickle
import numpy as np


# Create your views here.

def home(request):
    context = {}
    context['form'] = InputForm()
    if (request.method == "POST"):
        print(request.POST)
        
    return render(request,'cancer.html',context)

def result(request):
    data = []
    
    if (request.method == "POST"):
        
        for key in request.POST:
            if key not in ['csrfmiddlewaretoken']:
                data.append(eval(request.POST[key]))
    
    model = joblib.load(r'C:\Users\Raj\Desktop\ml-healthcare\ml_health\cancermodel\cancer_model')
    data = np.array(data).reshape(1,-1)
    predictions = model.predict(data)
    context ={}
    if (predictions[0]):
        context['predictions'] = 'Benign'
    else:
        context['predictions'] = 'Malignant'   
    
    
    
       
    return render(request,'result.html',context)