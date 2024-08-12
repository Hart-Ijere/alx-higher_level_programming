//  Use jQuery to select the DIV with the ID 'red_header' and bind a click event handler
$('#red_header').click(() => {
  // When the DIV is clicked, update the color of the header element to red (#FF0000)
  $('header').css('color', '#FF0000')
})

