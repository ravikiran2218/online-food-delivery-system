from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.food_list),
    path('order/', views.create_order),
]