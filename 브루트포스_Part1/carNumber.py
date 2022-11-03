def car(number, idx, last):
    if(len(number) == idx):
        # 입력한 형태의 마지막 위치에 도달했으면 1 반환(+1)
        return 1

    # c(문자)인 경우 아스키코드 값으로 a~z, 문자가 아니면 아스키코드 값으로 0~9
    start = ord('a') if number[idx] == 'c' else ord('0')
    end = ord('z') if number[idx] == 'c' else ord('9')

    ans = 0
    # 문자/숫자 중, 직전에 사용되지 않았으면 개수 +1
    for i in range(start, end+1):
        if i != last:
            ans += car(number, idx+1, i)
    return ans

number = input()
print(car(number, 0, ''))