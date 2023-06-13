#!/usr/bin/node
const ls = require('./100-data').list;
console.log(ls);
console.log(ls.map((item, index) => item * index));
