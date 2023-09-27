#!/usr/bin/node
const request = require('request');
const baseURL = 'https://swapi-api.alx-tools.com/api/';
request(baseURL + 'films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  function printCharacter(i) {
    if (i >= characters.length) {
      return;
    }
    request(characters[i], function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacter(i + 1);
    });
  }
  printCharacter(0);
});

