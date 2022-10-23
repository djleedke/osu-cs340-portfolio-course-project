from flask import Flask, render_template
from flask_mysqldb import MySQL
import config

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

@app.route('/')
def index():

    context = {}

    try:
        # Getting counts from each table to display the # of rows
        cursor = mysql.connection.cursor()
        query = (
            "SELECT" 
            "(SELECT COUNT(*) FROM chefs) as chefs,"
            "(SELECT COUNT(*) FROM dishes) as dishes,"
            "(SELECT COUNT(*) FROM dish_has_recipe) as dish_has_recipe,"
            "(SELECT COUNT(*) FROM ingredients) as ingredients,"
            "(SELECT COUNT(*) FROM recipes) as recipes,"
            "(SELECT COUNT(*) FROM recipe_has_ingredient) as recipe_has_ingredient,"
            "(SELECT COUNT(*) FROM restaurants) as restaurants"
        )

        cursor.execute(query)
        context = cursor.fetchall()[0]
    except Exception as e:
        print(e)

    return render_template('pages/index.html', context=context)

@app.route('/chefs')
def chefs():
    return render_template('pages/chefs.html')

@app.route('/dishes')
def dishes():
    return render_template('pages/dishes.html')

@app.route('/dish-has-recipe')
def dish_has_recipe():
    return render_template('pages/dish_has_recipe.html')

@app.route('/ingredients')
def ingredients():
    return render_template('pages/ingredients.html')

@app.route('/recipes')
def recipes():
    return render_template('pages/recipes.html')

@app.route('/recipe-has-ingredient')
def recipe_has_ingredient():
    return render_template('pages/recipe_has_ingredient.html')

@app.route('/restaurants')
def restaurants():
    return render_template('pages/restaurants.html')

if __name__ == '__main__':

    app.run(port=62134, debug=True)