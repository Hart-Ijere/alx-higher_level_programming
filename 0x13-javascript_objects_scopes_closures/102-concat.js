#!/usr/bin/node
// Concatenates 2 files

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

if (!file1 || !file2 || !destination) {
  console.error('Usage: ./concat-files.js <file1> <file2> <destination>');
  process.exit(1);
}

try {
  const data1 = fs.readFileSync(file1, 'utf8');
  const data2 = fs.readFileSync(file2, 'utf8');
  fs.writeFileSync(destination, data1 + data2);
} catch (err) {
  console.error(err);
  process.exit(1);
}
