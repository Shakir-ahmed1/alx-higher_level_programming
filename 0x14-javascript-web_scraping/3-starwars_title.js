#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const episode = JSON.parse(body);
    console.log(episode.title);
  }
}
);
