from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^ingredient/new/$', views.new_ingredient, name = 'new_ingredient'),
    url(r'^ingredients/$', views.list_ingredients, name = 'list_ingredients'),
    url(r'^item/new/$', views.new_item, name = 'new_item'),
    url(r'^items/$', views.list_items, name = 'list_items'),
    url(r'^$', TemplateView.as_view(template_name='log/home.html'), name = 'log_home'),
]
