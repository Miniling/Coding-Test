var fs = require('fs');
var input = fs.readFileSync(0).toString().trim().split('\n');

// 값 0이고 길이 10001인 배열 생성
var temp = Array.from({ length: 10001 }, () => 0);
const WN = input[0].split(' ');
var W = Number(WN[0]);
const N = Number(WN[1]);

// 금액에 해당하는 금속 무게 저장
for (var i = 1; i < input.length; i++) {
    var MP = input[i].split(' ');
    temp[Number(MP[1])] += Number(MP[0]);
}

// 금액 높은 순으로 금속 가져가기
var answer = 0;
for (var i = temp.length - 1; i > -1; i--) {
    if (temp[i] <= W) {
        answer += temp[i] * i;
        W -= temp[i];
    }
    // 가져갈 금속의 무게가 남은 무게보다 많으면 남은 만큼 가져가고 종료.
    else {
        answer += W * i;
        break;
    }
}

console.log(answer);