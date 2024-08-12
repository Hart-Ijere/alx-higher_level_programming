$(document).ready(() => {
        // Use jQuery to fetch the translation for "hello"
        $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
          // Update the text of the <div> element with the translation
          $('#hello').text(data.hello)
        })
      })
