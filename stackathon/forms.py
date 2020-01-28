from django import forms
from stackathon.models import Allergy, Prescription, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", 
        "last_name", 
        "email",
        "password",
        "birthday",)

class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ("allergy",)

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ("prescription",)