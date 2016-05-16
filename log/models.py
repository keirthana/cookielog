from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.name
        
class Dish(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    item = models.ForeignKey(Item)
    ingredients = models.ManyToManyField(Ingredient)
    
    def __str__(self):
        return self.name
        
