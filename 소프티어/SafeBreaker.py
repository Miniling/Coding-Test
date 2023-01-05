import sys

input = sys.stdin.readline

# 배낭 무게 W, 종류 N
W, N = map(int, input().split())

# 금속 무게 M, 가격 P
MP = []
for _ in range(N):
    MP.append(list(map(int, input().split())))

# 비싼 순으로 정렬
MP.sort(key=lambda e: -e[1])

cost, weight = 0, 0
for jew in MP:
    # 보석을 전부 담아도 남으면 전부 담기
    if weight+jew[0] < W:
        cost += jew[0]*jew[1]
        weight += jew[0]
    # 전부 담을 수 없으면 잘라서 담기
    else:
        cost += (W-weight)*jew[1]
        weight += (W-weight)

    if weight >= W:
        break

print(cost)