from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os, config

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/chefs')
def chefs():
    return render_template('pages/chefs.html')

@app.route('/dishes')
def dishes():
    return render_template('pages/dishes.html')

@app.route('/ingredients')
def ingredients():
    return render_template('pages/ingredients.html')

@app.route('/recipes')
def recipes():
    return render_template('pages/recipes.html')

@app.route('/restaurants')
def restaurants():
    return render_template('pages/restaurants.html')

if __name__ == '__main__':

    app.run(port=62134, debug=True)