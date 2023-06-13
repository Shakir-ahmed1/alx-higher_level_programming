#!/usr/bin/node
let len = 0;
process.argv.forEach((val, index) => {
  len++;
});
if (len === 2) console.log('No Argument');
else console.log(`${process.argv[2]}`);
