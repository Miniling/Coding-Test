test = int(input())

case = []
answer = []

# 홀수 더하기 계산
for i in range(test):
    case.append(list(map(int, input().split())))
    total = 0
    for j in range(len(case[i])):
        num = case[i][j]
        if(num%2 == 1):
            total += num

    answer.append(total)

# 출력
for i in range(test):
    print('#'+str(i+1)+' '+str(answer[i]))