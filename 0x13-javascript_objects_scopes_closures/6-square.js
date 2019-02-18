#!/usr/bin/node
let Sqr = require('./5-square');
class Square extends Sqr {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let row = 0; row < this.height; row++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
