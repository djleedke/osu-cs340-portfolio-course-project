from flask import Flask, render_template
from flask_mysqldb import MySQL
import config, database as db

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

@app.route('/')
def index():
    context = db.get_table_counts(mysql)[0]
    return render_template('pages/index.html', context=context)

@app.route('/chefs')
def chefs():
    context = db.get_all_chefs(mysql)
    return render_template('pages/chefs.html', context=context)

@app.route('/dishes')
def dishes():
    context = db.get_all_dishes(mysql)
    return render_template('pages/dishes.html', context=context)

@app.route('/dish-has-recipe')
def dish_has_recipe():
    context = db.get_all_dish_has_recipe(mysql)
    return render_template('pages/dish_has_recipe.html', context=context)

@app.route('/ingredients')
def ingredients():
    context = db.get_all_ingredients(mysql)
    return render_template('pages/ingredients.html', context=context)

@app.route('/recipes')
def recipes():
    context = db.get_all_recipes(mysql)
    return render_template('pages/recipes.html', context=context)

@app.route('/recipe-has-ingredient')
def recipe_has_ingredient():
    context = db.get_all_recipe_has_ingredient(mysql)
    return render_template('pages/recipe_has_ingredient.html', context=context)

@app.route('/restaurants')
def restaurants():
    context = db.get_all_restaurants(mysql)
    return render_template('pages/restaurants.html', context=context)

if __name__ == '__main__':

    app.run(port=62134, debug=True)