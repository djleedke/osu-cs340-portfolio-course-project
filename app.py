from flask import Flask, render_template, redirect, url_for, request, jsonify
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

    chefs = db.get_all_chefs(mysql)
    restaurants = db.get_all_restaurants(mysql)

    context = {
        'chefs': chefs,
        'restaurants' : restaurants
    }

    return render_template('pages/chefs.html', context=context)

@app.route('/chefs/<chef_id>')
def get_chef(chef_id):

    chef = db.get_chef(mysql, chef_id)
    return jsonify(chef)

@app.route('/chefs/insert', methods=['POST'])
def insert_chef():

    chef = {
        'name': request.form['name'],
        'position' : request.form['position'],
        'restaurant' : request.form['restaurant']
    }

    db.insert_chef(mysql, chef)
    return redirect(url_for('chefs'))

@app.route('/chefs/update', methods=['POST'])
def update_chef():

    chef = {
        'id' : request.form['chef-id'],
        'name': request.form['name'],
        'position' : request.form['position'],
        'restaurant_id' : request.form['restaurant']
    }

    db.update_chef(mysql, chef)
    return redirect(url_for('chefs'))

@app.route('/chefs/delete', methods=['DELETE'])
def delete_chef():
    db.delete_chef(mysql, request.json['chef_id'])
    return redirect(url_for('chefs'))

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