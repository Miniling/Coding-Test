// 입력 변수 생성
var fs = require('fs');

// 입력 받기(split하여 배열 형태로 저장)
var input = fs.readFileSync(0).toString().trim().split(' ');

var A = Number(input[0]);
var B = Number(input[1]);

// 삼항 연산자로 비교 및 출력
A > B ? console.log('A') : A < B ? console.log('B') : console.log('same');