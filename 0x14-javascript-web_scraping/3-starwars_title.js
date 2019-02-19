#!/usr/bin/node
// prints the title of a Star Wars movie where the ep no. matches an int
const request = require('request');
const epNum = process.argv[2];
const url = `http://swapi.co/api/films/${epNum}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
