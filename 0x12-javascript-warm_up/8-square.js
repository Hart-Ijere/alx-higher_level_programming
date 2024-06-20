#!/usr/bin/node

// Retrieve first argument passed to the script
const size = Number(process.argv[2]);

// Check if the converted value is a valid number and print the appropriate message
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Loop to print the square
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
