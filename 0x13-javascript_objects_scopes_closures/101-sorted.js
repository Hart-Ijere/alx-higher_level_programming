#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence

const { dict } = require('./101-data');

const newDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (newDict[occurrences] === undefined) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}

console.log(newDict);
