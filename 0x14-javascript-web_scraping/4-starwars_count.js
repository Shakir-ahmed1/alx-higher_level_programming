#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const response = JSON.parse(body);
    let count = 0;
    for (let index = 0; index < response.results.length; index++) {
      response.results[index].characters.forEach(element => { if (element.includes('/18/')) count++; }
      );
    }
    console.log(count);
  }
}
);
