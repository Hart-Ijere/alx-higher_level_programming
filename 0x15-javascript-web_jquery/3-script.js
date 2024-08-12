// Use jQuery to select the DIV with the ID 'red_header' and bind a click event handler
$('#red_header').click(() => {
  // When the DIV is clicked, add the class 'red' to the header element
  $('header').addClass('red')
})
