<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch Hello Translation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
      $(document).ready(() => {
        // Use jQuery to fetch the translation for "hello"
        $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
          // Update the text of the <div> element with the translation
          $('#hello').text(data.hello)
        })
      })
    </script>
</head>
<body>
    <div id="hello"></div>
</body>
</html>
