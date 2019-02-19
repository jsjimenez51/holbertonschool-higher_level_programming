#!/usr/bin/node
// computes the number of tasks completed by a user id from api
const request = require('request');
const url = process.argv[2];
let taskDict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let tasksList = JSON.parse(body);
    for (let task of tasksList) {
      if (task.completed === true) {
        let id = task.userId;

        if (taskDict[id] === undefined) {
          taskDict[id] = 1;
        } else {
          taskDict[id] += 1;
        }
      }
    }
    console.log(taskDict);
  }
});
