#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter(idx => idx === searchElement).length;
};
