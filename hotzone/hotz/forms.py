from django import forms
from django.forms import ModelForm, TextInput
from hotz.models import *

class geoDataForm(forms.ModelForm):
    class Meta():
        model = Location
        fields = ['nameEN', 'addressEN', 'xCoor', 'yCoor']
        widgets = {'nameEN' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Search location...'})}
        