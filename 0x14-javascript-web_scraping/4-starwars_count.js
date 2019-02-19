#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is there
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let data = JSON.parse(body);
    let movieData = (data.results);
    let wedgeID = /18/;

    for (let movie of movieData) {
      let chars = movie.characters;
      for (let isWedge of chars) {
        if (wedgeID.test(isWedge) === true) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
