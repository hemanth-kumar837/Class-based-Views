from django import forms

from app.models import *

class SchoolForm(forms.ModelForm):
    def Meta():
        model=School
        fields='__all__'