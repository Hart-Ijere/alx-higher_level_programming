#!/usr/bin/node

// Retrieve and convert command-line arguments
const args = process.argv.slice(2).map(Number);

// Check if there are less than 2 arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // Sort the arguments in descending order and find the second largest one
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
