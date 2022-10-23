
-- Insert queries for sample data --

-- restaurants --

INSERT INTO restaurants (name) VALUES 
("Doug's Bistro"),
("David's Fine Diner"),
("D&D's");

-- chefs -- 

INSERT INTO chefs (restaurant_id, name, position) VALUES
(1, "Doug Leedke", "Head Chef"),
(1, "Marcos Miller", "Sous Chef"),
(2, "David Harlan", "Head Chef"),
(2, "Lewis Griffith", "Sous Chef"),
(3, "Melissa Mcdonald", "Head Chef"),
(3, "Matt Robins", "Sous Chef");

-- ingredients --

INSERT INTO ingredients (name, type) VALUES
("Chicken Breast", "Protein"),
("Spaghetti", "Grain"),
("Egg", "Protein"),
("White Rice", "Grain"),
("Crab", "Protein"),
("Water", "Other"),
("Garlic", "Herbs & Spices");

-- dishes --

INSERT INTO dishes (name) VALUES 
    ("Meatloaf w/ Truffle Fries"),
    ("Firecracker Chicken & Steamed White Rice");

-- dish_has_recipe --

INSERT INTO dish_has_ recipe (dish_id, recipe_id) VALUES 
    (1, 2),
    (1, 6),
    (2, 7),
    (2, 5);

-- recipe_has_ingredient --

INSERT INTO recipe_has_ingredient (recipe_id, ingredient_id, quantity, measurement) VALUES 
    (1, 1, 4, "cups"),
    (1, 2, 1, "lb"),
    (1, 3, 3, "units"),
    (3, 4, 2, "cups"),
    (3, 5, 8, "pieces"),
    (7, 4, 2, "cups");

-- recipes --

INSERT INTO recipes (chef_id, name, cuisine, heat_level, gluten_free) VALUES 
    (5, "Chicken Carbonara", "Italian", 1, FALSE),
    (4, "Meatloaf", "American", 2, FALSE),
    (2, "California Rolls", "Japanese", 1, FALSE),
    (6, "Caprese Salad", "Italian", 1, TRUE),
    (3, "Firecracker Chicken", "Asian", 5, FALSE),
    (1, "Truffle Fries", "American", 1, FALSE),
    (2, "Steamed White Rice", "Asian", 1, FALSE);