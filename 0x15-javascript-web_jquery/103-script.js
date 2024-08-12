$(document).ready(() => {
        // Function to fetch and display the translation
        function fetchTranslation() {
          // Get the value from the input field with ID 'language_code'
          const languageCode = $('#language_code').val();
          
          // Construct the URL for the API request
          const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
          
          // Fetch the translation from the API
          $.get(url, (data) => {
            // Update the text of the <div> element with ID 'hello'
            $('#hello').text(data.hello);
          });
        }

        // Bind a click event to the button with ID 'btn_translate'
        $('#btn_translate').click(fetchTranslation);

        // Bind a keypress event to the input field with ID 'language_code'
        $('#language_code').keypress((event) => {
          // Check if the Enter key was pressed (key code 13)
          if (event.which === 13) {
            fetchTranslation(); // Call the function to fetch the translation
          }
        });
      });
