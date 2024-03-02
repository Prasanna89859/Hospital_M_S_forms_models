from django import forms
from app.models import *

class departmentForms(forms.ModelForm):
    class Meta():
        model=department
        fields='__all__'
        
class DoctorForms(forms.ModelForm):
    class Meta():
        model=Doctor
        fields='__all__'

class patientforms(forms.ModelForm):
    class Meta():
        model=patient
        fields='__all__'

class AM_forms(forms.ModelForm):
    class Meta():
        model=AM
        fields='__all__'






