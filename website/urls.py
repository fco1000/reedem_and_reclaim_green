from django.urls import path
from .views import home_view,objective_view,contact_view

urlpatterns = [
    path('',home_view,name='home'),
    path('objectives',objective_view,name='objectives'),
    path('contact',contact_view,name='contacts'),
]