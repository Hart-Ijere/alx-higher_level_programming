#!/bin/bash
# Send a DELETE request to the URL passed as the first argument and display the body of the response.
curl -s "$1" -X DELETE
