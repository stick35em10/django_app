from django import forms
from .models import Project

class ProjectoForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }