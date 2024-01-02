import json


def load_drinks():
    with open("drinks.json") as file:
        drinks = json.load(file)
    return drinks


def get_categories(drinks):
    categories = []
    for drink in drinks:
        if drink["category"] not in categories:
            categories.append(drink["category"])
    return categories


def get_flavor_profiles(drinks):
    flavor_profiles = []
    for drink in drinks:
        flavor_profiles = []
        if drink["flavor_profile"] not in flavor_profiles:
            flavor_profiles.append(drink["flavor_profile"])
    return flavor_profiles


def get_dietary_preferences(drinks):
    dietary_preferences = []
    for drink in drinks:
        for preference in drink["dietary_preferences"]:
            if preference not in dietary_preferences:
                dietary_preferences.append(preference)
    return dietary_preferences


def get_allergy_info(drinks):
    allergy_info = []
    for drink in drinks:
        for allergy in drink["allergy_info"]:
            if allergy not in allergy_info:
                allergy_info.append(allergy)
    return allergy_info
