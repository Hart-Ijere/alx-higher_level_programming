#!/usr/bin/node

// Import the original file where myVar is defined
require('./100-my_var');

// Modify the value of myVar
myVar = 333;

// Print the modified value of myVar
console.log(myVar);
