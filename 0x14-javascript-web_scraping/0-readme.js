#!/usr/bin/node
// const request = require('request');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) console.error(err);
  else console.log(data);
});
