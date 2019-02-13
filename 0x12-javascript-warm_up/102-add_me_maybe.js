#!/usr/bin/node
// function that increments and calls a function

exports.addMeMaybe = (number, theFunction) => {
  number = number + 1;
  theFunction(number);
};
