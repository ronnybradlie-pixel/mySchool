from django import forms
from .models import *


class schoolForm(forms.ModelForm):
    Teacher = forms.ModelChoiceField(queryset= Teacher.objects.all(), 
                                     empty_label="Select Teacher",)
    
    class Meta:
        model = School
        fields= ['school_name', 'address', 'location', 'teachers']

class TeacherForm(forms.ModelFom):
    class Meta:
        model=Teacher
        fields=['name', 'email', 'subject', 'image']    
        
            
