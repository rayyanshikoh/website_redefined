from django.db import models

# Create your models here.
class Heartdisease(models.Model):
    age = models.IntegerField(default=0)
    sex = models.IntegerField(default=0)
    cp = models.IntegerField(default=0)
    trestbps = models.IntegerField(default=0)
    chol = models.IntegerField(default=0)
    fbs = models.IntegerField(default=0)
    restecg = models.IntegerField(default=1)
    thalach = models.IntegerField(default=0)
    exang = models.IntegerField(default=0)
    oldpeak = models.IntegerField(default=0)
    slope = models.IntegerField(default=0)
    ca = models.IntegerField(default=0)
    thal = models.IntegerField(default=0)