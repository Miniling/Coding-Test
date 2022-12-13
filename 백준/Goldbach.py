# 테스트 케이스 개수 T
T = int(input())

# 에라토스테네스의 체
max_num = 10000
check = [0]*(max_num+1)
check[0] = check[1] = True
prime = []

# max_num까지 소수만 남기기
for i in range(2, max_num+1):
    if not check[i]:
        prime.append(i)
        j = i+i
        while j <= max_num:
            check[j] = True
            j += i

for _ in range(T):
    n = int(input())
    distance = []
    for a in prime:
        b = n-a
        # a가 b를 넘지 않는 값 까지만
        if (a <= b) and (check[b] == False):
            distance.append([a, b])

    # 마지막 항목이 두 소수의 차이가 가장 작음
    ab = distance.pop()
    a, b = ab[0], ab[1]
    print(a, b)