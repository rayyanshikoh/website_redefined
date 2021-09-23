from django import forms

class AiForm(forms.Form):
    age = forms.IntegerField(label="Age:")
    sex = forms.IntegerField(label="Sex:")
    cp = forms.IntegerField(label="cp:")
    trestbps = forms.IntegerField(label="trestbps")
    chol = forms.IntegerField(label="chol:")
    fbs = forms.IntegerField(label="fbs:")
    restecg = forms.IntegerField(label="restecg:")
    thalach = forms.IntegerField(label="thalach:")
    exang = forms.IntegerField(label="exang:")
    oldpeak = forms.IntegerField(label="oldpeak:")
    slope = forms.IntegerField(label="slope:")
    ca = forms.IntegerField(label="ca:")
    thal = forms.IntegerField(label="thal:")