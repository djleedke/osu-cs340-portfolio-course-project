-- get all Restaurant IDs and Names to populate the Restaurant dropdown
SELECT restaurant_id, name FROM restaurants
ORDER BY name ASC;

-- get all chefs and their position and restaurant for the Chefs page
SELECT chefs.chef_id, chefs.name, chefs.position, restaurants.name AS Restaurant 
FROM chefs 
    INNER JOIN restaurants ON chefs.restaurant_id = restaurants.restaurant_id
ORDER BY chefs.name ASC;

-- get a single chef's data for the Update Chef form
SELECT chefs.chef_id, chefs.name, chefs.position, chefs.restaurant_id
FROM chefs 
WHERE chefs.chef_id = :chef_ID_selected_from_browse_chefs_page;

-- get all ingredients to populate a dropdown for associating with recipes
SELECT ingredient_id AS ing_id, ingredients.name 
FROM ingredients
ORDER BY ingredients.name ASC;



-- add a new restaurant
INSERT INTO restaurants (name) 
    VALUES (:name);

-- add a new chef
INSERT INTO chefs (name, position, restaurant_id) 
    VALUES (:name, :position, :restaurant_id);

-- add a new recipe
INSERT INTO recipes (name, cuisine, heat_level, gluten_free, description)
    VALUES (:name, :cuisine, :heat_level, :gluten_free, :description);

-- add a new dish
INSERT INTO dishes (name, rating)
    VALUES (:name, :rating);

-- add a new ingredient
INSERT INTO ingredients (name, type)
    VALUES (:name, :type);

-- associate a dish with recipes (M-to-M relationship addition)
INSERT INTO dish_has_recipe (did, rid) 
VALUES (:dish_id_from_dropdown_input, :recipe_id_from_dropdown_input);

-- associate a recipe with ingredients (M-to-M relationship addition)
INSERT INTO recipe_has_ingredients (rid, iid) 
VALUES (:recipe_id_from_dropdown_input, :ingredient_id_from_dropdown_input);

-- update a chef's data based on submission of the Update Chef form 
UPDATE chefs
SET name = :name_input, position= :position_input, restaurant_id = :restaurant_id_from_dropdown_input 
WHERE chefs.chef_id= :chef_id_from_the_update_form;

-- delete a dish
DELETE FROM dishes 
WHERE dishes.dish_id = :dish_id_selected_from_dropdown_input;

-- dis-associate a certificate from a person (M-to-M relationship deletion)
DELETE FROM dish_has_recipe
WHERE did = :dish_id_selected_from_dish_and_recipe_list 
    AND rid = :recipe_id_selected_from_dish_and_recipe_list;
