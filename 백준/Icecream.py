# 어떤 종류의 아이스크림이 포함되면 맛이 없어짐.
# 그러한 경우를 피하면서 아이스크림 3가지 선택
# 선택 방법 개수 구하기

import itertools

# 종류 N, 섞으면 안 되는 조합 개수 M
n, m = map(int, input().split())

# 2차원 조합표
icecream = []
for i in range(n):
    line = []
    for _ in range(n):
        line.append(False)
    icecream.append(line)

# 섞으면 안 되는 조합 표시
for i in range(m):
    i1, i2 = map(int, input().split())
    icecream[i1 - 1][i2 - 1] = True
    icecream[i2 - 1][i1 - 1] = True

ans = 0
# 배열 인덱스 상, 한 자리씩 내려가므로 범위가 1~5이면 0~4로 되도록 iter를 범위로 지정
for i in itertools.combinations(range(n), 3):
    # 안 되는 조합이 있으면 넘김
    if icecream[i[0]][i[1]] or icecream[i[0]][i[2]] or icecream[i[1]][i[2]]:
        continue
    ans += 1

print(ans)