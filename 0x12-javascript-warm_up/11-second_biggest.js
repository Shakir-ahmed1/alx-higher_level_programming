#!/usr/bin/node
const len = process.argv.length;
let first, second;
if (len <= 3) {
  console.log(0);
} else {
  if (Number(process.argv[2]) > Number(process.argv[3])) {
    first = process.argv[2];
    second = process.argv[3];
  } else {
    first = process.argv[3];
    second = process.argv[2];
  }
  for (let i = 4; i < len; i++) {
    if (Number(process.argv[i]) > Number(first)) {
      second = first;
      first = process.argv[i];
    }
  }
  console.log(second);
}
