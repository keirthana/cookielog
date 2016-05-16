from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewIngredientForm
from .models import Ingredient

def new_ingredient(request):
    if request.method == 'POST':
        form = NewIngredientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingredient saved successfully')
            return redirect('list_ingredients')
    else:
        form = NewIngredientForm()
    return render(request, 'log/new_ingredient.html', {'form' : form})
    
def list_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'log/list_ingredients.html', {'ingredients' : ingredients})
    
    

