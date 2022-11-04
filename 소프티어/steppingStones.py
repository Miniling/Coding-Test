import sys

N = int(input())
A = list(map(int, input().split()))

# 위치 별 디딤 수
steps = [1] * N
for i in range(1, N):
    # 위치 별 최대 이동 가능 수
    max_steps = 0

    # 이전 위치와 최대 이동 가능 수 비교
    for j in range(i):
        if (A[j] < A[i] and max_steps < steps[j]):
            max_steps = steps[j]

    steps[i] = max_steps + 1

print(max(steps))