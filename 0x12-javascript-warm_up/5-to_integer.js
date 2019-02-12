#!/usr/bin/node
// prints a statement if the first arg passed can be converted to an integer

if (parseInt(process.argv[2])) {
  console.log(`My number: ${parseInt(process.argv[2])}`);
} else {
  console.log('Not a number');
}
