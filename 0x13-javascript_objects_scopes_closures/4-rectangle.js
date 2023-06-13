#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) return {};
    else {
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
module.exports = Rectangle;
