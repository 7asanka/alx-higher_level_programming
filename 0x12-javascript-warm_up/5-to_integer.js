#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
console.log(!isNaN(num) ? `My number: ${num}` : 'Not a number');
