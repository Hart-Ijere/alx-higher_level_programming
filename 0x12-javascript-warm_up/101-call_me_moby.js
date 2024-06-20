#!/usr/bin/node

// Import the callMeMoby function from 15-call_function_x_times.js
const callMeMoby = require('./15-call_function_x_times');

// Define a simple function to be called
const printMessage = () => {
  console.log('Hello, world!');
};

// Call the function 5 times
callMeMoby(5, printMessage);
