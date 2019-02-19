#!/usr/bin/node
// writes a string to a file
let fs = require('fs');
let file = process.argv[2];
let data = process.argv[3];

fs.writeFile(file, data, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
