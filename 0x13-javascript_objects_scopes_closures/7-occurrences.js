#!/usr/bin/node
// Return the number of occurrences of an element in a list

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, currentElement) => {
    return (currentElement === searchElement) ? count + 1 : count;
  }, 0);
};
