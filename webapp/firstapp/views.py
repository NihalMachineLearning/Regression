from django.shortcuts import render
import joblib
import json,os
import numpy as np
import pandas as pd
import psycopg2
#from .models import Internship
# Create your views here.

def index(request):
    return render(request,'index.html')

def result(request):
    model = joblib.load('../models/model.joblib')
    list =[]
    list.append(float(request.GET('age')))
    list.append(float(request.GET('sex')))
    list.append(float(request.GET('bmi')))
    list.append(float(request.GET('children')))
    list.append(float(request.GET('smoker')))
    list.append(float(request.GET('region')))
    
    
    
    answer = model.predict(([list]).tolist())[0]
    
    b = internship(age=request.Get['age'],sex=request.Get['sex'],bmi=request.Get['bmi'],children=request.Get['children'],smoker=request.Get['smoker'],region=request.Get['region'],charges=answer)
    b.save()
    return render(request,'index.html',{
        'answer':answer
    })
