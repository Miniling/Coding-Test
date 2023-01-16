var fs = require('fs');
var input = fs.readFileSync(0).toString().trim().split('\n');

const test = Number(input[0]);

for (var i = 1; i < input.length; i++) {
    var value = input[i].split(' ');
    console.log(`Case #${i}: ${Number(value[0]) + Number(value[1])}`);
}