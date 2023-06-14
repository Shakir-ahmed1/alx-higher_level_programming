#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (letter) {
    let temp = '';
    if (typeof letter === 'undefined') {
      letter = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        temp += letter;
      }
      console.log(temp);
      temp = '';
    }
  }
}
module.exports = Square;
