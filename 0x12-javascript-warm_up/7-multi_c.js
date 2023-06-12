#!/usr/bin/node
const iter = Number(process.argv[2]);
let i;
if (isNaN(iter)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < iter; i++) console.log('C is fun');
}
