# 킹1, 퀸1, 룩2, 비숍2, 나이트2, 폰8개 = 총 16개
oneset = [1, 1, 2, 2, 2, 8]

# 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰 개수
white = list(map(int, input().split()))

ans = []
for i in range(len(white)):
    a, b = oneset[i], white[i]
    if a==b:
        ans.append(0)
    else:
        ans.append(a-b)

for chess in ans:
    print(chess, end=' ')