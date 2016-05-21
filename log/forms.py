from django import forms
from .models import Ingredient, Item

class NewIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name',]

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name',]        
        
