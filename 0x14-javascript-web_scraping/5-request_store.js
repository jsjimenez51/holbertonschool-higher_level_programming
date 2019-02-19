#!/usr/bin/node
// gets the content of a webpage and stores it in a file
const request = require('request');
const url = process.argv[2];
const fPath = process.argv[3];
let fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let data = body;
    fs.writeFile(fPath, data, function (error, file) {
      if (error) {
        console.log(error);
      }
    });
  }
});
