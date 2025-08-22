from django.shortcuts import render

def index(request):
    return render(request, "core/index.html", context={})

def cat_food(request):
    cat_food_one = "Shutki"
    cat_food_two = "Purina"
    cat_food_three = "Pro Plan"

    cat_food = [cat_food_one, cat_food_two, cat_food_three]
    return render(request, "core/cat_food.html", context={'cat_food': cat_food_one,})