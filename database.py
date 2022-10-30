
def execute_query(mysql, query):
    """Wrapper function to assist with querying the database."""
    
    data = {}

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

    except Exception as e:
        print(e)

    return data

# ---------- Miscellaneous ----------
def get_table_counts(mysql):
    """Returns the number of rows for each table in the database."""

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
    return execute_query(mysql, query)

# --------- chefs ---------
def get_all_chefs(mysql):
    """Returns all rows from the chefs table."""

    query = ("SELECT * FROM chefs")
    return execute_query(mysql, query)

# ---------- dishes ----------
def get_all_dishes(mysql):
    """Returns all rows from the dishes table."""

    query = ("SELECT * FROM dishes")
    return execute_query(mysql, query)

# ---------- dish_has_recipe ---------
def get_all_dish_has_recipe(mysql):
    """Returns all rows from the dish_has_recipe table."""

    query = ("SELECT * FROM dish_has_recipe" )
    return execute_query(mysql, query)

# ---------- ingredients ----------
def get_all_ingredients(mysql):
    """Returns all rows from the ingredients table."""

    query = ("SELECT * FROM ingredients")
    return execute_query(mysql, query)

# --------- recipes ----------
def get_all_recipes(mysql):
    """Returns all rows from the recipes table."""
    
    query = ("SELECT * FROM recipes")
    return execute_query(mysql, query)

# --------- recipe_has_ingredient ---------
def get_all_recipe_has_ingredient(mysql):
    """Returns all rows from the recipe_has_ingredient table."""

    query = ("SELECT * FROM recipe_has_ingredient")
    return execute_query(mysql, query)

# ---------- restaurants ----------
def get_all_restaurants(mysql):
    """Returns all rows from the restaurants table."""
    
    query = ("SELECT * FROM restaurants")
    return execute_query(mysql, query)