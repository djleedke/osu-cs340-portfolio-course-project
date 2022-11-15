

// Setting up onchange listeners for our update forms (to fill them in dynamically)

if(document.getElementById('updateChef')){
    document.getElementById('updateChef').onchange = function() {

        let chefId = document.getElementById('updateChef').value;
    
        fetch("/chefs/" + chefId, {
            method: 'GET',
            headers: {
                'Content-Type' : 'application/json'
            }
        }).then(response => response.json())
        .then( data => {
            document.getElementById('updateName').value = data[0].name;
            document.getElementById('updatePosition').value = data[0].position;
    
            restaurantId = data[0].restaurant_id === null ? "NULL" : data[0].restaurant_id;
            document.getElementById('updateRestaurant').value = restaurantId;
    
        });
    }
}

if(document.getElementById('updateRestaurant')){
    document.getElementById('updateRestaurant').onchange = function() {

        let restaurantId = document.getElementById('updateRestaurant').value;
    
        fetch("/restaurants/" + restaurantId, {
            method: 'GET',
            headers: {
                'Content-Type' : 'application/json'
            }
        }).then(response => response.json())
        .then( data => {
            document.getElementById('updateRestaurantName').value = data[0].name;
        });
    }
}

/**
 * Sends a DELETE request for the provided chefId, 
 * removes it from the database, and reloads the page.
 * 
 * @param {string} chefId 
 */
function deleteChef(chefId) {

    fetch("/chefs/delete", {
        method: 'DELETE',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({ 'chef_id' : chefId })
    }).then(() => {
        location.reload()
    });

};

/**
 * Sends a DELETE request for the provided dishId, 
 * removes it from the database, and reloads the page.
 * 
 * @param {string} dishId 
 */
 function deleteDish(dishId) {

    fetch("/dishes/delete", {
        method: 'DELETE',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({ 'dish_id' : dishId })
    }).then(() => {
        location.reload()
    });

};

/**
 * Sends a DELETE request for the provided dishId, 
 * removes it from the database, and reloads the page.
 * 
 * @param {string} dishId 
 */
 function deleteDishHasRecipe(dishId, recipeId) {

    fetch("/dish-has-recipe/delete", {
        method: 'DELETE',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({ 
            'dish_id' : dishId,
            'recipe_id' : recipeId 
        })
    }).then(() => {
        location.reload()
    });

};

/**
 * Sends a DELETE request for the provided restaurantId, 
 * removes it from the database, and reloads the page.
 * 
 * @param {string} restaurantId 
 */
function deleteRestaurant(restaurantId) {
    fetch("/restaurants/delete", {
        method: 'DELETE',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({ 'restaurant_id' : restaurantId })
    }).then(() => {
        location.reload()
    });
};


/**
 * Sends a DELETE request for the provided ingredientId, 
 * removes it from the database, and reloads the page.
 * 
 * @param {string} ingredientId 
 */
 function deleteIngredient(ingredientId) {

    fetch("/ingredients/delete", {
        method: 'DELETE',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({ 'ingredient_id' : ingredientId })
    }).then(() => {
        location.reload()
    });

};

/**
 * Sends a DELETE request for the provided recipeId, 
 * removes it from the database, and reloads the page.
 * 
 * @param {string} recipeId 
 */
 function deleteRecipe(recipeId) {

    fetch("/recipes/delete", {
        method: 'DELETE',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({ 'recipe_id' : recipeId })
    }).then(() => {
        location.reload()
    });

};

/**
 * Sends a DELETE request for the provided recipeID and ingredientID, 
 * removes it from the database, and reloads the page.
 * 
 * @param {string} recipeId, ingredientID
 */
 function deleteRecipeHasIngredient(recipeId, ingredientId) {

    fetch("/recipe-has-ingredient/delete", {
        method: 'DELETE',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({ 
            'recipe_id' : recipeId,
            'ingredient_id' : ingredientId 
        })
    }).then(() => {
        location.reload()
    });

};
