from django import forms
from .models import Ingredient

class NewIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name',]
        
        
