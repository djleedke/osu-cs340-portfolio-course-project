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
    return render_template('index.html')

if __name__ == '__main__':

    app.run(port=62134, debug=True)