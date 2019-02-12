#!/usr/bin/node
// searches for the second biggest int in a list of args

if (process.argv.length <= 3) {
  console.log('0');
} else {
  console.log(process.argv
    .slice(2)
    .sort((a, b) => (a - b))
    .reverse()[1]
  );
}
