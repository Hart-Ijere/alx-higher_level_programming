// Use jQuery to select the DIV with the ID 'add_item' and bind a click event handler
$('#add_item').click(() => {
  // Create a new <li> element with the text "Item"
  const newItem = $('<li>Item</li>')
  
  // Append the new <li> element to the UL with class 'my_list'
  $('ul.my_list').append(newItem)
})
