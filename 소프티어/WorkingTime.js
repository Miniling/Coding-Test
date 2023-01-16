var fs = require('fs');

// '\n'단위로 끊어서 배열 형태로 저장
var input = fs.readFileSync(0).toString().trim().split('\n');

var answer = 0;
input.map(e => {
    answer += ((Number(e[6] + e[7]) - Number(e[0] + e[1])) * 60 + (Number(e[9] + e[10]) - Number(e[3] + e[4])));
});

console.log(answer);