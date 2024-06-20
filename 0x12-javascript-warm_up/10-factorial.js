#!/usr/bin/node

// Define the recursive factorial function
function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Retrieve and convert argument passed to the script
const n = Number(process.argv[2]);

// Check if the argument is a valid number
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
