-- The character ':' will be used to denote variables that will be passed into the query.

----- Restaurants Table -----

-- get all restaurants
SELECT * FROM restaurants;

-- get all Restaurant IDs and Names to populate the Restaurant dropdown
SELECT restaurant_id, name FROM restaurants
ORDER BY name ASC;

-- add a new restaurant
INSERT INTO restaurants (name) 
    VALUES (:name);

-- update a restaurant
UPDATE restaurants SET name = :restaurant_name_from_input
WHERE restaurant_id = :restaurant_id_from_input;

-- delete a restaurant
DELETE FROM restaurants WHERE restaurant_id = :restaurant_id_from_input;


----- Chefs Table -----

-- get all chefs
SELECT * FROM chefs;

-- get specific chef
SELECT * FROM chefs WHERE chef_id=:chef_id;

-- get all chefs and their position and restaurant for the Chefs page
SELECT chefs.chef_id, chefs.name, chefs.position, restaurants.name AS Restaurant 
FROM chefs 
    LEFT JOIN restaurants ON chefs.restaurant_id = restaurants.restaurant_id;

-- get a single chef's data for the Update Chef form
SELECT chefs.chef_id, chefs.name, chefs.position, chefs.restaurant_id
FROM chefs 
WHERE chefs.chef_id = :chef_ID_selected_from_browse_chefs_page;

-- add a new chef
INSERT INTO chefs (name, position, restaurant_id) 
    VALUES (:name, :position, :restaurant_id);

-- update chef information
UPDATE chefs SET name = :chef_name_input, position = :chef_position_input, 
    restaurant_id = :restaurant_id_from_input
WHERE chef_id = :chef_id_from_input;

-- delete a chef
DELETE FROM chefs WHERE chef_id = :chef_id_from_input;


----- Recipes Table -----

-- get all recipes
SELECT * FROM recipes;

-- get all recipes w/ chef name included
SELECT recipes.*, chefs.name as chef_name FROM recipes LEFT JOIN chefs ON chefs.chef_id=recipes.recipe_id;

-- search recipes by name
SELECT * FROM recipes
WHERE recipes.name LIKE "% :recipe_name_input %";

-- add a new recipe
INSERT INTO recipes (name, cuisine, heat_level, gluten_free, description)
    VALUES (:name, :cuisine, :heat_level, :gluten_free, :description);

-- update a recipe
UPDATE recipes SET name = :recipe_name_from_input, cuisine = :cuisine_from_input,
    heat_level = :heat_level_from_input, gluten_free = :gluten_free_from_input,
    description = :description_from_input, chef_id = :chef_id_from_input
WHERE recipe_id = :recipe_id_input;

-- delete a recipe
DELETE FROM recipes WHERE recipe_id = :recipe_id_from_input;


----- Ingredients Table -----

-- get all ingredients
SELECT * FROM ingredients;

-- get all ingredients to populate a dropdown for associating with recipes
SELECT ingredient_id AS ing_id, ingredients.name 
FROM ingredients
ORDER BY ingredients.name ASC;

-- add a new ingredient
INSERT INTO ingredients (name, type)
    VALUES (:name, :type);

-- update an ingredient
UPDATE ingredients
SET name = :name_input, type = :type_input
WHERE ingredient_id = :ingredient_id_input;

-- delete an ingredient
DELETE FROM ingredients
WHERE ingredient_id = :ingredient_id_input;


----- Dishes Table -----

-- get all dishes
SELECT * FROM dishes;

-- add a new dish
INSERT INTO dishes (name, rating)
    VALUES (:name, :rating);

-- update a dish
UPDATE dishes
SET name = :name_input, rating = :rating_input
WHERE dish_id = :dish_id_input;

-- delete a dish
DELETE FROM dishes 
WHERE dish_id = :dish_id_input;


----- Recipe_Has_Ingredient Table -----

-- get table
SELECT * FROM recipe_has_ingredient;

-- get table w/ ingredient & recipe names
SELECT recipe_has_ingredient.*, recipes.name as recipe_name, ingredients.name as ingredient_name FROM recipe_has_ingredient 
	LEFT JOIN recipes ON recipes.recipe_id=recipe_has_ingredient.recipe_id
    LEFT JOIN ingredients ON ingredients.ingredient_id=recipe_has_ingredient.ingredient_id;

-- associate a recipe with ingredients (M-to-M relationship addition)
INSERT INTO recipe_has_ingredient (recipe_id, ingredient_id, quantity, measurement) 
VALUES (:recipe_id_input, :ingredient_id_input, :quantity_input, :measurement_input);

-- update an ingredient for a recipe
UPDATE recipe_has_ingredient
SET recipe_id = :recipe_id_input, ingredient_id = :ingredient_id_input,
quantity = :quantity_input, measurement = :measurement_input
WHERE recipe_id = :recipe_id_input AND ingredient_id = :ingredient_id_input; -- Need to make this id?

-- delete ingredient for a recipe
DELETE FROM recipe_has_ingredient
WHERE recipe_id = :recipe_id_input AND ingredient_id = :ingredient_id_input;


----- Dish_Has_Recipe Table -----

-- get table
SELECT * FROM dish_has_recipe;

-- get table w/ dish & recipe names
SELECT dish_has_recipe.*, dishes.name as dish_name, recipes.name as recipe_name
FROM dish_has_recipe
    LEFT JOIN dishes ON dish_has_recipe.dish_id=dishes.dish_id
    LEFT JOIN recipes ON dish_has_recipe.recipe_id=recipes.recipe_id;

-- associate a dish with recipes (M-to-M relationship addition)
INSERT INTO dish_has_recipe (dish_id, recipe_id) 
VALUES (:dish_id_input, :recipe_id_input);

-- update a dish_has_recipe entry
UPDATE dish_has_recipe
SET dish_id = :dish_id_input, recipe_id = :recipe_id_input
WHERE dish_id = :dish_id_input AND recipe_id = :recipe_id_input;

