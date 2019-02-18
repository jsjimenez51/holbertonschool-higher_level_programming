#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  while (list.length) {
    newList.push(list.pop());
  }
  return newList;
};
