from flask import Flask, render_template
import utils

drinks = utils.load_drinks()
categories = utils.get_categories(drinks)
flavor_profiles = utils.get_flavor_profiles(drinks)
dietary_preferences = utils.get_dietary_preferences(drinks)
allergy_info = utils.get_allergy_info(drinks)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html', drinks=drinks)


app.run(host='0.0.0.0', port=81)
