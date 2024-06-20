#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Retrieve and convert the first and second arguments passed to the script
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

// Check if the arguments are valid numbers and print the result of the addition
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
