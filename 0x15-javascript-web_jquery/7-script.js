// Use jQuery to select the DIV with the ID 'character' and fetch the character name
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
  // Update the text of the <div> element with the character name
  $('#character').text(data.name)
})
