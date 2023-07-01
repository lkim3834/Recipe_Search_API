import random
import requests
import pyodide_http
from pyscript import Element
from js import document, DOMParser, setInterval
pyodide_http.patch_all()

meal = Element('meal')
meal_details = Element('meal-details-content')


def get_random_recipe(searchInputTxt):
    response = requests.get(
        'https://www.themealdb.com/api/json/v1/1/filter.php?i=chicken_breast'
    )
    data = response.json()
    # recipe = data['meals'][0]
    meal.write(searchInputTxt)
    for key, value in data.items():
        print(key)
        for i in range(len(value)):
            print(value[i]['strMeal'])
    return data
    # return "Hello World"


def generate_recipe():
    searchInputTxt = document.getElementById('search').value
    recipe = get_random_recipe(searchInputTxt)
    print(recipe)

    # print("Title: " + recipe['strMeal'])
    # print("Category: " + recipe['strCategory'])
    # print("Instructions: " + recipe['strInstructions'])
    # print("Ingredients:")
    # for i in range(1, 21):
    #     ingredient = recipe['strIngredient' + str(i)]
    #     measure = recipe['strMeasure' + str(i)]
    #     if ingredient:
    #         print("- " + measure + " " + ingredient)
