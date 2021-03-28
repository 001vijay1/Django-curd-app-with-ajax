from django import forms
from .models import Abc

        
class AbcForm(forms.ModelForm):
    class Meta:
        model = Abc
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'age': forms.TextInput(attrs={'class':'form-control','id':'ageid'}),
            'score': forms.TextInput(attrs={'class':'form-control','id':'scoreid'})
        }