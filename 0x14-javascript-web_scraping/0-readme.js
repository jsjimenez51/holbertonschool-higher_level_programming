#!/usr/bin/node
// reads and prints the content of a file
let fPath = process.argv[2];
let fs = require('fs');

fs.readFile(fPath, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
