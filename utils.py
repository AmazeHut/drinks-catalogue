import json


def load_drinks():
    with open("drinks.json") as file:
        drinks = json.load(file)
    return drinks


def get_categories(drinks):
    categories = []
    for drink in drinks:
        if drink["category"] not in categories:
            categories.append(drink["category"].lower())
    return categories


def get_flavor_profiles(drinks):
    flavor_profiles = []
    for drink in drinks:
        if drink["flavor_profile"] not in flavor_profiles:
            flavor_profiles.append(drink["flavor_profile"].lower())
    return flavor_profiles


def get_ingredients(drinks):
    ingredients = []
    for drink in drinks:
        for ingredient in drink["ingredients"]:
            if ingredient.lower() not in ingredients:
                ingredients.append(ingredient.lower())
    return ingredients


def get_dietary_preferences(drinks):
    dietary_preferences = []
    for drink in drinks:
        for preference in drink["dietary_preferences"]:
            if preference.lower() not in dietary_preferences:
                dietary_preferences.append(preference.lower())
    return dietary_preferences


def get_allergy_info(drinks):
    allergy_info = []
    for drink in drinks:
        for allergy in drink["allergy_info"]:
            if allergy.lower() not in allergy_info:
                print(allergy_info)
                allergy_info.append(allergy.lower())
    return allergy_info
