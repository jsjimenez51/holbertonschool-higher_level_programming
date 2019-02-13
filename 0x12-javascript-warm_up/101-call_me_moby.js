#!/usr/bin/node
// executes an external function x times

exports.callMeMoby = (x, theFunction) => {
  let i = x;
  while (i > 0) {
    theFunction();
    --i;
  }
};
