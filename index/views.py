from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
import joblib
import numpy as np


# Create your views here.

def home(request):
    context = {}
    return render(request,'index.html',context)