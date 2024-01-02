from flask import Flask, render_template, request 
import utils

drinks = utils.load_drinks()
categories = utils.get_categories(drinks)
flavor_profiles = utils.get_flavor_profiles(drinks)
dietary_preferences = utils.get_dietary_preferences(drinks)
allergy_info = utils.get_allergy_info(drinks)

app = Flask(__name__)

nav_menu = {
    "Category": categories,
    "Flavor": flavor_profiles,
    "Diet": dietary_preferences,
    "Allergy": allergy_info,
}

print(nav_menu)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', drinks=drinks, menu=nav_menu)

@app.route('/search')
def search():
    search_term = request.args.get('q').lower()
    selected_drinks = []
    for drink in drinks:
        for elem in drink.values():
            if search_term in str(elem).lower():
                if drink not in selected_drinks:
                    selected_drinks.append(drink)
            
    return render_template('home.html', drinks=selected_drinks, menu=nav_menu)


@app.route('/category/<category>')
def category(category):
    if category in categories:
        selected_drinks = [
            drink for drink in drinks if drink['category'].lower() == category.lower()]
        return render_template('home.html', drinks=selected_drinks, menu=nav_menu)
    else:
        return "Category not found"


@app.route('/flavor/<flavor_profile>')
def flavor_profile(flavor_profile):
    if flavor_profile in flavor_profiles:
        selected_drinks = [
            drink for drink in drinks if drink['flavor_profile'].lower() == flavor_profile.lower()]
        return render_template('home.html', drinks=selected_drinks, menu=nav_menu)
    else:
        return "Flavor profile not found"


@app.route('/diet/<dietary_preference>')
def dietary_preference(dietary_preference):
    if dietary_preference in dietary_preferences:
        selected_drinks = [
            drink for drink in drinks if dietary_preference in list(map(str.lower, drink['dietary_preferences']))]
        return render_template('home.html', drinks=selected_drinks, menu=nav_menu)
    else:
        return "Dietary preference not found"


@app.route('/allergy/<allergy>')
def allergy(allergy):
    if allergy in allergy_info:
        selected_drinks = [
            drink for drink in drinks if allergy in list(map(str.lower, drink['allergy_info']))]
        return render_template('home.html', drinks=selected_drinks, menu=nav_menu)
    else:
        return "Allergy not found"


if __name__ == '__main__':
    app.run(port=5000)
