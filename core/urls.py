from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cat-food", views.cat_food, name="cat-food"),
]