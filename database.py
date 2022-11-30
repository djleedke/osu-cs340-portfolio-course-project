
def execute_query(mysql, query, values=None):
    """Wrapper function to assist with querying the database."""

    # Reference: https://github.com/osu-cs340-ecampus/flask-starter-app
    # Scope: Line
    # Date: 10/23/2022
    # Originality: Adapted
    # Adapted database connection and query execution example to create this function.
    
    data = {}

    try:
        cursor = mysql.connection.cursor()

        if(values):
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        
        data = cursor.fetchall()

        # If it was an insert no data will be returned, returning
        # the id of the row that was inserted instead
        if len(data) == 0:
            data = (cursor.lastrowid)
        
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

    query = (f"DELETE FROM chefs WHERE chef_id = {chef_id}")

    return execute_query(mysql, query)

# ---------- dishes ----------
def get_all_dishes(mysql):
    """Returns all rows from the dishes table."""

    query = ("SELECT * FROM dishes")
    return execute_query(mysql, query)

def insert_dish(mysql, dish):
    """"Inserts a dish into the dishes table and creates a many-to-many row in
    dish_has_recipe for any provided recipe_ids."""

    # Adding null when rating is empty
    if(dish['rating'] == ''):
        dish['rating'] = 'NULL'

    query = (
        f"INSERT INTO dishes (name, rating) VALUES ('{dish['name']}', {dish['rating']});"
    )

    dish_id = execute_query(mysql, query)

    # Iterating recipes and inserting each of those in dish_has_recipe
    for recipe_id in dish['recipes']:
        insert_dish_has_recipe(mysql, dish_id, recipe_id)

    return dish_id

def delete_dish(mysql, dish_id):
    """Deletes a dish from the dishes table for the specified dish_id."""

    query = (f"DELETE FROM dishes WHERE dish_id = {dish_id};")

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

def insert_dish_has_recipe(mysql, dish_id, recipe_id):
    """Inserts a row into the dish_has_recipe table."""

    query = (
        "INSERT INTO dish_has_recipe (dish_id, recipe_id) "
            f"VALUES ('{dish_id}', '{recipe_id}');"
    )

    return execute_query(mysql, query)

def delete_dish_has_recipe(mysql, dish_id, recipe_id):
    """Deletes a row from the dish_has_recipe table."""

    query = (
        "DELETE FROM dish_has_recipe "
        f"WHERE dish_id = {dish_id} AND recipe_id = {recipe_id}"
    )

    return execute_query(mysql, query)

# ---------- ingredients ----------
def get_all_ingredients(mysql):
    """Returns all rows from the ingredients table."""

    query = ("SELECT * FROM ingredients")
    return execute_query(mysql, query)

def insert_ingredient(mysql, ingredient):
    """Inserts an ingredient into the ingredients table.  Must provide an ingredient dictionary that contains the table attributes."""

    query = (
        "INSERT INTO ingredients (name, type)"
        f" VALUES ('{ingredient['name']}', '{ingredient['type']}');"
    )

    return execute_query(mysql, query)

def delete_ingredient(mysql, ingredient_id):
    """Deletes an ingredient from the ingredients table for the specified ingredient_id."""

    query = (f"DELETE FROM ingredients WHERE ingredient_id = {ingredient_id};")

    return execute_query(mysql, query)

# --------- recipes ----------
def get_all_recipes(mysql):
    """Returns all rows from the recipes table."""
    
    query = (
        "SELECT recipes.*, chefs.name as chef_name FROM recipes "
            "LEFT JOIN chefs ON recipes.chef_id=chefs.chef_id;"
    )

    return execute_query(mysql, query)

def search_recipe(mysql, search):

    # Handles if chef is empty but recipe name is filled out
    if search['chef-id'] == "":
        query = (
        "SELECT recipes.*, chefs.name as chef_name FROM recipes "
        "LEFT JOIN chefs ON recipes.chef_id=chefs.chef_id "
        f"WHERE recipes.name LIKE '%{search['recipe_name']}%'"
        )
        return execute_query(mysql, query)

    elif search['recipe_name'] == "":
        query = (
        "SELECT recipes.*, chefs.name as chef_name FROM recipes "
        "LEFT JOIN chefs ON recipes.chef_id=chefs.chef_id "
        f"WHERE recipes.chef_id={search['chef-id']};"
        )
        return execute_query(mysql, query)

    # Handles if both recipe name and chef are selected for search
    else:

        query = (
        "SELECT recipes.*, chefs.name as chef_name FROM recipes "
        "LEFT JOIN chefs ON recipes.chef_id=chefs.chef_id "
        f"WHERE recipes.chef_id = {search['chef-id']} AND recipes.name LIKE '%{search['recipe_name']}%'"
        )

        return execute_query(mysql, query)

def insert_recipe(mysql, recipe):
    """Inserts a recipe into the recipes table.  Must provide a recipe dictionary that contains the table attributes."""

    # Reference: https://stackoverflow.com/questions/10950362/protecting-against-sql-injection-in-python
    # Scope: Line
    # Date: 11/27/2022
    # Originality: Adapted
    # Referenced to rework execute_query to prevent sql injection and escape quotes

    if(recipe['heat_level'] == ''):
        recipe['heat_level'] = None

    query = (
        "INSERT INTO recipes (name, chef_id, cuisine, heat_level, gluten_free, description)"
        " VALUES (%s, %s, %s, %s, %s, %s);"
    )

    values = (recipe['name'], recipe['chef'], recipe['cuisine'], recipe['heat_level'], recipe['gluten_free'], recipe['description'])
    
    return execute_query(mysql, query, values)

def delete_recipe(mysql, recipe_id):
    """Deletes a recipe from the recipes table for the specified recipe_id."""

    query = (f"DELETE FROM recipes WHERE recipe_id = {recipe_id};")

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

def insert_recipe_has_ingredient(mysql, recipe_has_ingredient):
    """Inserts a row into the recipe_has_ingredient table."""

    query = (
        "INSERT INTO recipe_has_ingredient (recipe_id, ingredient_id, quantity, measurement) "
            f"VALUES ({recipe_has_ingredient['recipe_id']}, {recipe_has_ingredient['ingredient_id']}, {recipe_has_ingredient['quantity']}, '{recipe_has_ingredient['measurement']}');"
    )

    return execute_query(mysql, query)

def delete_recipe_has_ingredient(mysql, recipe_id, ingredient_id):
    """Deletes a row from the recipe_has_ingredient table."""

    query = (
        "DELETE FROM recipe_has_ingredient "
        f"WHERE recipe_id = {recipe_id} AND ingredient_id = {ingredient_id}"
    )

    return execute_query(mysql, query)

# ---------- restaurants ----------
def get_all_restaurants(mysql):
    """Returns all rows from the restaurants table."""
    
    query = ("SELECT * FROM restaurants")
    return execute_query(mysql, query)

def get_restaurant(mysql, restaurant_id):
    """Returns the restaurant for the given restaurant_id"""

    query = (
        f"SELECT * FROM restaurants WHERE restaurant_id={restaurant_id};"
    )

    return execute_query(mysql, query)

def insert_restaurant(mysql, restaurant):
    """Inserts a new restaurant into the restaurants table.  Must provide a restaurant dictionary that contains the table attributes."""

    query = (
        "INSERT INTO restaurants (name)"
        f" VALUES ('{restaurant['name']}');"
    )

    return execute_query(mysql, query)

def update_restaurant(mysql, restaurant):
    """Updates the restaurant with the provided values and id"""

    query = (
        f'UPDATE restaurants SET name="{restaurant["name"]}" '
        f"WHERE restaurant_id='{restaurant['id']}';"
    )

    return execute_query(mysql, query)

def delete_restaurant(mysql, restaurant_id):
    """Deletes a restaurant from the restaurants table for the specified restaurant_id."""

    query = (f"DELETE FROM restaurants WHERE restaurant_id = {restaurant_id}")

    return execute_query(mysql, query)
