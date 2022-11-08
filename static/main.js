

// Setting up onchange listeners for our update forms (to fill them in dynamically)
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