# 첫째 줄에 N의 진짜 약수의 개수
N = int(input())

# 둘째 줄에 N의 진짜 약수
measure = list(map(int, input().split()))

# N= 1*N, (1 다음 큰 수 * N 다음 작은 수), ...
answer = (min(measure) * max(measure))
print(answer)