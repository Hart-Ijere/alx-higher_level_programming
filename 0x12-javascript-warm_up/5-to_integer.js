#!/usr/bin/node

// Retrieve first argument passed to the script
const arg = process.argv[2];

// Convert argument to a number
const num = Number(arg);

// Check if the converted value is a valid number and print the appropriate message
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
