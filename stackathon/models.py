from django.db import models

# Create your models here.
class Allergy(models.Model):
    allergy = models.CharField(blank=False, max_length=30)
    pass

class Prescription(models.Model):
    prescription = models.CharField(blank=False, max_length=30)
    pass
    
# class Contraindication(models.Model):
#     prescription = models.ForeignKey(Prescription)
#     allergy = models.ForeignKey(Allergy)
#     contraindication_text = models.TextField(blank=False)

class User(models.Model):
    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    email = models.EmailField(blank=False)
    password = models.CharField(blank=False, max_length=30)
    birthday = models.DateField(blank=True)
    allergies = models.ManyToManyField(Allergy)
    prescriptions = models.ManyToManyField(Prescription)


