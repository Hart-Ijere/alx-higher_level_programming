 $(document).ready(() => {
        // Add a new <li> element to the list
        $('#add_item').click(() => {
          const newItem = $('<li>Item</li>');  // Create a new <li> element
          $('ul.my_list').append(newItem);    // Append it to UL with class 'my_list'
        });

        // Remove the last <li> element from the list
        $('#remove_item').click(() => {
          $('ul.my_list li').last().remove();  // Select the last <li> and remove it
        });

        // Clear all <li> elements from the list
        $('#clear_list').click(() => {
          $('ul.my_list').empty();  // Remove all child elements from UL with class 'my_list'
        });
      });
