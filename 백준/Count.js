var fs = require('fs');
var input = fs.readFileSync("./count.txt").toString().trim();
input = input.split('\n');

console.log(input);