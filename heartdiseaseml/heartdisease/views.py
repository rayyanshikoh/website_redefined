from django.shortcuts import render
import xgboost as xgb
import numpy as np
import pickle
import sklearn
# Create your views here.

from django.http import HttpResponse

with open('./heartdisease/models/heart.pkl', 'rb') as f:
    clf_xgb = pickle.load(f)

def query(data):
    ans = clf_xgb.predict(data)
    return ans
    

def index(request):
    return render(request, './heartdisease/index.html')

def results(request):
    age = request.POST.get("age")
    sex = request.POST.get("sex")
    cp = request.POST.get("cp")
    trestbps = request.POST.get("trestbps")
    chol = request.POST.get("chol")
    thalach = request.POST.get("thalach")
    exang = request.POST.get('exang')
    oldpeak = request.POST.get("oldpeak")
    slope = request.POST.get("slope")
    ca = request.POST.get("ca")
    thal = request.POST.get("thal")
    print(age)
    if age != 0:
        age = int(age)
        sex = float(sex)
        cp = int(cp)
        trestbps = int(trestbps)
        chol = int(chol)
        thalach = int(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)
        data = np.array([[age, sex, cp, trestbps, chol, thalach, exang, oldpeak, slope, ca, thal]])
        result = str((query(data)))[1:2]
        if result == '0':
            result = "seems unlikely"
        elif result == '1':
            result = "Seems likely"
        else:
            result = "something went wrong, please try again!"

        return render(request, "./heartdisease/results.html", {"result": result})

