# 규칙1. 선택한 포도주는 모두 마시고, 잔은 원래 위치에 둘 것.
# 규칙2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 가능한 많은 양의 포도주를 맛보기 위한 선택
# 첫째 줄에 잔의 개수 n
# 둘째 줄부터 n+1번째 줄까지 잔에 든 양이 순서대로 부여

n = int(input())

total = [0]*(n+1)
wine = [0]

for _ in range(n):
    wine.append(int(input()))

# D[1] = A[1] 첫 잔을 마신 경우
total[1] = wine[1]
# D[2] = A[1] + A[2] 처음 두 잔을 마신 경우
if n >= 2:
    total[2] = wine[1] + wine[2]

for i in range(3, n+1):
    total[i] = total[i-1]
    # 직전의 잔을 건너뛰고 현재의 잔을 선택했을 때 값이 더 큰 경우
    if total[i] < (total[i-2] + wine[i]):
        total[i] = total[i-2] + wine[i]

    # 두개 전의 잔을 건너뛰고 직전과 현재의 잔을 선택했을 때 값이 더 큰 경우
    if total[i] < (total[i-3] + wine[i] + wine[i-1]):
        total[i] = total[i-3] + wine[i] + wine[i-1]

print(max(total))