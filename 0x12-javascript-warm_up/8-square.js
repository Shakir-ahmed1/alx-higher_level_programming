#!/usr/bin/node
const num = Number(process.argv[2]);
let temp = '';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    temp = '';
    for (let j = 0; j < num; j++) {
      temp += 'X';
    }
    console.log(temp);
  }
}
