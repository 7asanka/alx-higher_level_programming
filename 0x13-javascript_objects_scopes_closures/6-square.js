#!/usr/bin/node
const SSquare = require('./5-square');
module.exports = class Square extends SSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
