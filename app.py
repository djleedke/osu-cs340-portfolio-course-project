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

# --------- chefs ---------

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
    result = db.delete_chef(mysql, request.json['chef_id'])
    return jsonify(result)

# --------- dishes ----------

@app.route('/dishes')
def dishes():

    context = {
        'dishes' : db.get_all_dishes(mysql),
        'recipes' : db.get_all_recipes(mysql)
    }

    return render_template('pages/dishes.html', context=context)

@app.route('/dishes/insert', methods=['POST'])
def insert_dish():

    # Reference: https://www.geeksforgeeks.org/how-to-get-data-from-immutablemultidict-in-flask/
    # Date Accessed: 11/13/2022
    # Referenced to get the list of recipes from the form in request.form.getlist('recipes')

    dish = {
        'name': request.form['name'],
        'rating' : request.form['rating'],
        'recipes' : request.form.getlist('recipes')
    }

    db.insert_dish(mysql, dish)
    return redirect(url_for('dishes'))

@app.route('/dishes/delete', methods=['DELETE'])
def delete_dish():
    result = db.delete_dish(mysql, request.json['dish_id'])
    return jsonify(result)


# ---------- dish_has_recipe ---------

@app.route('/dish-has-recipe')
def dish_has_recipe():

    context = {
        'recipes' : db.get_all_recipes(mysql),
        'dishes' : db.get_all_dishes(mysql),
        'dish_has_recipe' : db.get_all_dish_has_recipe(mysql)
    }

    return render_template('pages/dish_has_recipe.html', context=context)

@app.route('/dish-has-recipe/insert', methods=['POST'])
def insert_dish_has_recipe():

    dish_has_recipe = {
        'dish_id': request.form['dish-id'],
        'recipe_id' : request.form['recipe-id'],
    }

    db.insert_dish_has_recipe(mysql, request.form['dish-id'], request.form['recipe-id'])
    return redirect(url_for('dish_has_recipe'))

@app.route('/dish-has-recipe/delete', methods=['DELETE'])
def delete_dish_has_recipe():
    result = db.delete_dish_has_recipe(mysql, request.json['dish_id'], request.json['recipe_id'])
    return jsonify(result)

# --------- ingredients ---------

@app.route('/ingredients')
def ingredients():
    context = db.get_all_ingredients(mysql)
    return render_template('pages/ingredients.html', context=context)

@app.route('/ingredients/insert', methods=['POST'])
def insert_ingredient():

    ingredient = {
        'name': request.form['name'],
        'type' : request.form['type']
    }

    db.insert_ingredient(mysql, ingredient)
    return redirect(url_for('ingredients'))

@app.route('/ingredients/delete', methods=['DELETE'])
def delete_ingredient():
    result = db.delete_ingredient(mysql, request.json['ingredient_id'])
    return jsonify(result)

# --------- recipes ---------

@app.route('/recipes')
def recipes():

    context = {
        'recipes' : db.get_all_recipes(mysql),
        'chefs' : db.get_all_chefs(mysql)
    }
    #context = db.get_all_recipes(mysql)
    return render_template('pages/recipes.html', context=context)

@app.route('/recipes/search', methods=['POST'])
def search_recipe():

    search = dict(request.form)
    results = db.search_recipe(mysql, search)

    return results

@app.route('/recipes/insert', methods=['POST'])
def insert_recipe():

    recipe = {
        'name': request.form['name'],
        'chef' : request.form['chef_id'],
        'cuisine' : request.form['cuisine'],
        'heat_level' : request.form['heat_level'],
        'gluten_free' : request.form['gluten_free'],
        'description' : request.form['description']                                     
    }
    db.insert_recipe(mysql, recipe)
    return redirect(url_for('recipes'))

@app.route('/recipes/delete', methods=['DELETE'])
def delete_recipe():
    result = db.delete_recipe(mysql, request.json['recipe_id'])
    return jsonify(result)

# ----------- recipe_has_ingredient ---------

@app.route('/recipe-has-ingredient')
def recipe_has_ingredient():
    context = {
        'recipe_has_ingredient' : db.get_all_recipe_has_ingredient(mysql),
        'recipes' : db.get_all_recipes(mysql),
        'ingredients' : db.get_all_ingredients(mysql)
    }
    #context = db.get_all_recipe_has_ingredient(mysql)
    return render_template('pages/recipe_has_ingredient.html', context=context)

@app.route('/recipe-has-ingredient/insert', methods=['POST'])
def insert_recipe_has_ingredient():

    recipe_has_ingredient = {
        'recipe_id': request.form['recipe-id'],
        'ingredient_id' : request.form['ingredient-id'],
        'quantity' : request.form['quantity'],
        'measurement' : request.form['measurement']
    }

    db.insert_recipe_has_ingredient(mysql, recipe_has_ingredient)
    return redirect(url_for('recipe_has_ingredient'))

@app.route('/recipe-has-ingredient/delete', methods=['DELETE'])
def delete_recipe_has_ingredient():
    result = db.delete_recipe_has_ingredient(mysql, request.json['recipe_id'], request.json['ingredient_id'])
    return jsonify(result)

# --------- restaurants --------- 

@app.route('/restaurants')
def restaurants():
    context = db.get_all_restaurants(mysql)
    return render_template('pages/restaurants.html', context=context)

@app.route('/restaurants/<restaurant_id>')
def get_restaurant(restaurant_id):

    restaurant = db.get_restaurant(mysql, restaurant_id)
    return jsonify(restaurant)

@app.route('/restaurants/insert', methods=['POST'])
def insert_restaurant():

    restaurant = {
        'name': request.form['name']
    }

    db.insert_restaurant(mysql, restaurant)
    return redirect(url_for('restaurants'))

@app.route('/restaurants/update', methods=['POST'])
def update_restaurant():

    restaurant = {
        'id' : request.form['restaurant-id'],
        'name': request.form['name']
    }

    db.update_restaurant(mysql, restaurant)
    return redirect(url_for('restaurants'))

@app.route('/restaurants/delete', methods=['DELETE'])
def delete_restaurant():
    result = db.delete_restaurant(mysql, request.json['restaurant_id'])
    return jsonify(result)

if __name__ == '__main__':

    app.run(port=62134, debug=True)
