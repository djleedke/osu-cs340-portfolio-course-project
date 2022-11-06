
def execute_query(mysql, query):
    """Wrapper function to assist with querying the database."""
    
    data = {}

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.connection.commit()
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

    #query = ("SELECT * FROM chefs")
    query = (
        "SELECT chefs.chef_id, chefs.name, chefs.position, restaurants.name as restaurant_name FROM chefs "
        "LEFT JOIN restaurants ON chefs.restaurant_id = restaurants.restaurant_id;"
    )
    
    return execute_query(mysql, query)

def get_chef(mysql, chef_id):
    """Returns the chef for the given chef_id"""

    query = (
        f"SELECT * FROM chefs WHERE chef_id={chef_id};"
    )

    return execute_query(mysql, query)

def insert_chef(mysql, chef):
    """Inserts a chef into the chefs table.  Must provide a chef dictionary that contains the table attributes."""

    query = (
        "INSERT INTO chefs (name, position, restaurant_id)"
        f" VALUES ('{chef['name']}', '{chef['position']}', {chef['restaurant']});"
    )

    return execute_query(mysql, query)

def update_chef(mysql, chef):

    query = (
        f"UPDATE chefs SET name='{chef['name']}', position='{chef['position']}', restaurant_id={chef['restaurant_id']} "
        f"WHERE chef_id={chef['id']};"
    )

    return execute_query(mysql, query)

def delete_chef(mysql, chef_id):
    """Deletes a chef from the chefs table for the specified chef_id."""

    print(chef_id)
    query = (f"DELETE FROM chefs WHERE chef_id = {chef_id}")

    return execute_query(mysql, query)

# ---------- dishes ----------
def get_all_dishes(mysql):
    """Returns all rows from the dishes table."""

    query = ("SELECT * FROM dishes")
    return execute_query(mysql, query)

# ---------- dish_has_recipe ---------
def get_all_dish_has_recipe(mysql):
    """Returns all rows from the dish_has_recipe table."""

    query = (
        "SELECT dish_has_recipe.*, dishes.name as dish_name, recipes.name as recipe_name "
        "FROM dish_has_recipe "
            "LEFT JOIN dishes ON dish_has_recipe.dish_id=dishes.dish_id "
            "LEFT JOIN recipes ON dish_has_recipe.recipe_id=recipes.recipe_id;"
    )

    return execute_query(mysql, query)

# ---------- ingredients ----------
def get_all_ingredients(mysql):
    """Returns all rows from the ingredients table."""

    query = ("SELECT * FROM ingredients")
    return execute_query(mysql, query)

# --------- recipes ----------
def get_all_recipes(mysql):
    """Returns all rows from the recipes table."""
    
    query = (
        "SELECT recipes.*, chefs.name as chef_name FROM recipes "
            "LEFT JOIN chefs ON chefs.chef_id=recipes.recipe_id;"
    )

    return execute_query(mysql, query)

# --------- recipe_has_ingredient ---------
def get_all_recipe_has_ingredient(mysql):
    """Returns all rows from the recipe_has_ingredient table."""

    query = (
        "SELECT recipe_has_ingredient.*, recipes.name as recipe_name, ingredients.name as ingredient_name "
        "FROM recipe_has_ingredient "
            "LEFT JOIN recipes ON recipes.recipe_id=recipe_has_ingredient.recipe_id "
            "LEFT JOIN ingredients ON ingredients.ingredient_id=recipe_has_ingredient.ingredient_id;"    
    )

    return execute_query(mysql, query)

# ---------- restaurants ----------
def get_all_restaurants(mysql):
    """Returns all rows from the restaurants table."""
    
    query = ("SELECT * FROM restaurants")
    return execute_query(mysql, query)