#!/usr/bin/node

// Check if first argument exists
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
