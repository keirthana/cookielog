from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewIngredientForm, NewItemForm
from .models import Ingredient, Item

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
    
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item saved successfully')
            return redirect('list_items')
    else:
        form = NewItemForm()
        return render(request, 'log/new_item.html', {'form' : form})
        
def list_items(request):
    items = Item.objects.all()
    return render(request, 'log/list_items.html', {'items' : items })
        
        
          
    
    

