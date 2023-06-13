#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let temp = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        temp += 'X';
      }
      console.log(temp);
      temp = '';
    }
  }

  rotate () {
    this.width = [this.height, this.height = this.width][0];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (letter = 'X') {
    let temp = '';
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
