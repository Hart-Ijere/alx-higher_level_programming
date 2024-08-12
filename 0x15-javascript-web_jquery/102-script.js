$(document).ready(() => {
        // Bind a click event to the button with ID 'btn_translate'
        $('#btn_translate').click(() => {
          // Get the value from the input field with ID 'language_code'
          const languageCode = $('#language_code').val();
          
          // Construct the URL for the API request
          const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
          
          // Fetch the translation from the API
          $.get(url, (data) => {
            // Update the text of the <div> element with ID 'hello'
            $('#hello').text(data.hello);
          });
        });
      });
