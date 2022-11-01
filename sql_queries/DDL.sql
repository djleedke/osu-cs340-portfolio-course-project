
SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- Table structure for table `restaurants`

DROP TABLE IF EXISTS `restaurants`;
CREATE TABLE `restaurants` (
  `restaurant_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`restaurant_id`),
  UNIQUE KEY `restaurant_id_UNIQUE` (`restaurant_id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
);

-- Inserting `restaurants` data

INSERT INTO `restaurants` VALUES 
(1, "D&D\'s"),
(2, "David\'s Fine Diner"),
(3, "Doug\'s Bistro");

-- Table structure for table `chefs`

DROP TABLE IF EXISTS `chefs`;
CREATE TABLE `chefs` (
  `chef_id` int(11) NOT NULL AUTO_INCREMENT,
  `restaurant_id` int(11),
  `name` varchar(255) NOT NULL,
  `position` varchar(50) NOT NULL,
  PRIMARY KEY (`chef_id`),
  UNIQUE KEY `chef_id_UNIQUE` (`chef_id`),
  FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`restaurant_id`)
);

-- Inserting `chefs` data

INSERT INTO `chefs` VALUES 
(1,(SELECT restaurant_id FROM restaurants WHERE name="Doug\'s Bistro"),'Doug Leedke','Head Chef'),
(2,(SELECT restaurant_id FROM restaurants WHERE name="D&D\'s"),'Marcos Miller','Sous Chef'),
(3,(SELECT restaurant_id FROM restaurants WHERE name="David\'s Fine Diner"),'David Harlan','Head Chef'),
(4,(SELECT restaurant_id FROM restaurants WHERE name="David\'s Fine Diner"),'Lewis Griffith','Sous Chef'),
(5,(SELECT restaurant_id FROM restaurants WHERE name="Doug\'s Bistro"),'Melissa Mcdonald','Head Chef'),
(6,(SELECT restaurant_id FROM restaurants WHERE name="Doug\'s Bistro"),'Matt Robins','Sous Chef'),
(7, NULL, 'Mandy Barnard', 'Sous Chef');

-- Table structure for table `dishes`

DROP TABLE IF EXISTS `dishes`;
CREATE TABLE `dishes` (
  `dish_id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` int(11) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`dish_id`),
  UNIQUE KEY `dish_id_UNIQUE` (`dish_id`)
);

-- Inserting `dishes` data

INSERT INTO `dishes` VALUES 
(1, 3,'Meatloaf w/ Truffle Fries'),
(2, NULL,'Firecracker Chicken & Steamed White Rice'),
(3, NULL, 'Chicken Carbonara & Caprese Salad');

-- Table structure for table `recipes`

DROP TABLE IF EXISTS `recipes`;
CREATE TABLE `recipes` (
  `recipe_id` int(11) NOT NULL AUTO_INCREMENT,
  `chef_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `cuisine` varchar(255) NOT NULL,
  `heat_level` int(11) DEFAULT NULL,
  `gluten_free` tinyint(4) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  PRIMARY KEY (`recipe_id`),
  UNIQUE KEY `recipe_id_UNIQUE` (`recipe_id`),
  KEY `fk_recipes_chefs1_idx` (`chef_id`),
  CONSTRAINT `fk_recipes_chefs1` FOREIGN KEY (`chef_id`) REFERENCES `chefs` (`chef_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Inserting `recipes` data

INSERT INTO `recipes` VALUES 
(1, (SELECT chef_id FROM chefs WHERE name='Melissa Mcdonald') ,'Chicken Carbonara','Italian',1,0,NULL),
(2, (SELECT chef_id FROM chefs WHERE name='Lewis Griffith'),'Meatloaf','American',2,0,NULL),
(3, (SELECT chef_id FROM chefs WHERE name='Marcos Miller'),'California Rolls','Japanese',1,0,NULL),
(4, (SELECT chef_id FROM chefs WHERE name='Matt Robins'),'Caprese Salad','Italian',1,1,NULL),
(5, (SELECT chef_id FROM chefs WHERE name='David Harlan'),'Firecracker Chicken','Asian',5,0,NULL),
(6, (SELECT chef_id FROM chefs WHERE name='Doug Leedke'),'Truffle Fries','American',1,0,NULL),
(7, (SELECT chef_id FROM chefs WHERE name='Marcos Miller'),'Steamed White Rice','Asian',1,0,NULL);

-- Table structure for table `dish_has_recipe`

DROP TABLE IF EXISTS `dish_has_recipe`;
CREATE TABLE `dish_has_recipe` (
  `dish_id` int(11) NOT NULL,
  `recipe_id` int(11) NOT NULL,
  PRIMARY KEY (`recipe_id`,`dish_id`),
  KEY `fk_dish_has_recipe_recipe1_idx` (`recipe_id`),
  KEY `fk_dish_has_recipe_dish1_idx` (`dish_id`),
  CONSTRAINT `fk_dish_has_recipe_recipe1` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`recipe_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_dish_has_recipe_dish1` FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`dish_id`) ON DELETE CASCADE ON UPDATE NO ACTION
);

-- Inserting `dish_has_recipe` data

INSERT INTO `dish_has_recipe` VALUES 
((SELECT dish_id FROM dishes WHERE name='Meatloaf w/ Truffle Fries'), (SELECT recipe_id FROM recipes WHERE name='Meatloaf')),
((SELECT dish_id FROM dishes WHERE name='Firecracker Chicken & Steamed White Rice'), (SELECT recipe_id FROM recipes WHERE name='Firecracker Chicken')),
((SELECT dish_id FROM dishes WHERE name='Meatloaf w/ Truffle Fries'), (SELECT recipe_id FROM recipes WHERE name='Truffle Fries')),
((SELECT dish_id FROM dishes WHERE name='Firecracker Chicken & Steamed White Rice'), (SELECT recipe_id FROM recipes WHERE name='Steamed White Rice')),
((SELECT dish_id FROM dishes WHERE name='Chicken Carbonara & Caprese Salad'), (SELECT recipe_id FROM recipes WHERE name='Chicken Carbonara')),
((SELECT dish_id FROM dishes WHERE name='Chicken Carbonara & Caprese Salad'), (SELECT recipe_id FROM recipes WHERE name='Caprese Salad'));


-- Table structure for table `ingredients`

DROP TABLE IF EXISTS `ingredients`;
CREATE TABLE `ingredients` (
  `ingredient_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  PRIMARY KEY (`ingredient_id`),
  UNIQUE KEY `ingredient_id_UNIQUE` (`ingredient_id`)
);

-- Inserting `ingredient` data

INSERT INTO `ingredients` VALUES 
(1,'Chicken Breast','Protein'),
(2,'Spaghetti','Grain'),
(3,'Egg','Protein'),
(4,'White Rice','Grain'),
(5,'Crab','Protein'),
(6,'Water','Other'),
(7,'Garlic','Herbs & Spices');

-- Table structure for table `recipe_has_ingredient`

DROP TABLE IF EXISTS `recipe_has_ingredient`;
CREATE TABLE `recipe_has_ingredient` (
  `recipe_id` int(11) NOT NULL,
  `ingredient_id` int(11) NOT NULL,
  `quantity` decimal(10,1) NOT NULL,
  `measurement` varchar(50) NOT NULL,
  PRIMARY KEY (`recipe_id`,`ingredient_id`),
  KEY `fk_recipe_has_ingredient_ingredient1_idx` (`ingredient_id`),
  KEY `fk_recipe_has_ingredient_recipe1_idx` (`recipe_id`),
  CONSTRAINT `fk_recipe_has_ingredient_recipe1` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`recipe_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_ingredient_ingredient1` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Inserting `recipe_has_ingredient` data

INSERT INTO `recipe_has_ingredient` VALUES 
((SELECT recipe_id FROM recipes WHERE name='Chicken Carbonara'), (SELECT ingredient_id FROM ingredients WHERE name='Chicken Breast'), 4, 'cups'),
((SELECT recipe_id FROM recipes WHERE name='Chicken Carbonara'), (SELECT ingredient_id FROM ingredients WHERE name='Spaghetti'),1.5,'lb'),
((SELECT recipe_id FROM recipes WHERE name='Chicken Carbonara'), (SELECT ingredient_id FROM ingredients WHERE name='Egg'),3,'units'),
((SELECT recipe_id FROM recipes WHERE name='California Rolls'), (SELECT ingredient_id FROM ingredients WHERE name='White Rice'),2,'cups'),
((SELECT recipe_id FROM recipes WHERE name='California Rolls'), (SELECT ingredient_id FROM ingredients WHERE name='Crab'),8,'pieces'),
((SELECT recipe_id FROM recipes WHERE name='Steamed White Rice'), (SELECT ingredient_id FROM ingredients WHERE name='White Rice'),2,'cups');

SET FOREIGN_KEY_CHECKS=1;
COMMIT;
