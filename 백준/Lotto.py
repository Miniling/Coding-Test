# 1 ~ 49에서 6개 선택
# k개를 골라 집합 S를 만들어 그 범위 내에서 번호 선택
# 테스트 케이스는 각 줄
# 각 줄의 첫 번째 원소는 개수 k
# 각 줄의 나머지 원소는 집합 S에 포함되는 숫자들
# 마지막 줄에 주어진 0은 테스트 케이스 종료

import itertools

COUNT = 6

while True:
    answer = list(map(int, input().split()))
    k = answer[0]
    numbers = []

    if k==0:
        break
    else:
        for i in range(1, len(answer)):
            numbers.append(answer[i])

        for lotto in itertools.combinations(numbers, 6):
            lotto = list(lotto)
            lotto.sort()
            for num in lotto:
                print(num, end=' ')
            print()     # 줄 띄우기

    # 테스트 케이스 별로 구분
    print()