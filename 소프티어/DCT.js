var dct = 0
for (var i = 0; i < input.length - 1; i++) {
    if (Number(input[i + 1]) == Number(input[i]) + 1) {
        dct = 1;
    } else if (Number(input[i]) - 1 == Number(input[i + 1])) {
        dct = -1;
    } else {
        dct = 0;
        // 중간에 어긋나고 다시 순서대로 가는 것 방지
        break;
    }
}

dct == 1 ? console.log('ascending') : dct == -1 ? console.log('descending') : console.log('mixed');