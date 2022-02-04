from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
import joblib
from .forms import InputForm
import numpy as np


# Create your views here.

def home(request):
    context = {}
    context['form'] = InputForm()
    if (request.method == "POST"):
        print(request.POST)
        
    return render(request,'kidney.html',context)

def result(request):
    data = []
    
    if (request.method == "POST"):
        
        for key in request.POST:
            if key not in ['csrfmiddlewaretoken']:
                data.append(eval(request.POST[key]))
    
    model = joblib.load(r'C:\Users\Raj\Desktop\ml-healthcare\ml_health\kidney\kidneymodel\kidney')
    data = np.array(data).reshape(1,-1)
    predictions = model.predict(data)
    context ={}
    if (predictions[0]):
        context['predictions'] = 'Congrats ! You are Healthy'
    else:
        context['predictions'] = 'Sorry,Suffering'   
    
    
    
       
    return render(request,'result.html',context)