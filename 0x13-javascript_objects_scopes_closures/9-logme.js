#!/usr/bin/node
let argVal = 0;

exports.logMe = function (item) {
  console.log(`${argVal}: ${item}`);
  argVal++;
};
