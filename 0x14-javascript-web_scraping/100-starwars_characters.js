#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.characters.length; i++) {
      request(data.characters[i], (e, r, b) => {
        if (e) {
          console.error(e);
        } else {
          const person = JSON.parse(b);
          console.log(person.name);
        }
      }
      );
    }
  }
}
);
