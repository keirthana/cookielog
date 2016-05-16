from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^ingredient/new/$', views.new_ingredient, name = 'new_ingredient'),
    url(r'^ingredients/$', views.list_ingredients, name = 'list_ingredients'),
]
