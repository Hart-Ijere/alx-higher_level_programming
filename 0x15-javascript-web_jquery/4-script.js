// Use jQuery to select the DIV with the ID 'toggle_header' and bind a click event handler
$('#toggle_header').click(() => {
  // Select the header element
  const header = $('header')
  
  // Toggle the class based on the current class
  if (header.hasClass('red')) {
    header.removeClass('red').addClass('green')
  } else {
    header.removeClass('green').addClass('red')
  }
})
