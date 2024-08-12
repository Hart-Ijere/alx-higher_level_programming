// Use jQuery to fetch the list of movies from the API
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  // Loop through each film in the fetched data
  data.results.forEach((film) => {
    // Create a new <li> element for each movie title
    const listItem = $('<li></li>').text(film.title)
    
    // Append the new <li> element to the UL with ID 'list_movies'
    $('#list_movies').append(listItem)
  })
})
