#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.err(err);
  } else {
    const todos = JSON.parse(body);
    const result = {};
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].userId in result) {
        if (todos[i].completed === true) result[todos[i].userId] += 1;
      } else {
        result[todos[i].userId] = 1;
      }
    }
    console.log(result);
  }
}
);
