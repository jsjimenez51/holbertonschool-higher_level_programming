#!/usr/bin/node
// prints a square

let size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let idx = size; idx > 0; idx--) {
    console.log('X'.repeat(size));
  }
}
