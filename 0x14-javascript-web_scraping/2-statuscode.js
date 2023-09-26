#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) console.error(err);
  else console.log('code:', response.statusCode);
});
