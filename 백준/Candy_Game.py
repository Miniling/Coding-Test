# 인접한 두 칸을 고른다.
# 사탕을 교환한다.

N = int(input())

# 맵 생성
map = []
for i in range(N):
    line = []
    colors = input()
    for j in range(len(colors)):
        line.append(colors[j])
    map.append(line)

def check(map):
    max_r, max_c = 1, 1
    for i in range(N):
        c = map[i][0]
        count_r = 1
        # 행 최대 개수
        for j in range(1, N):
            if map[i][j] == c:
                count_r += 1
                if count_r > max_r:
                    max_r = count_r
            else:
                c = map[i][j]
                count_r = 1

    for j in range(N):
        r = map[0][j]
        count_c = 1
        # 열 최대 개수
        for i in range(1, N):
            if map[i][j] == r:
                count_c += 1
                if count_c > max_c:
                    max_c = count_c
            else:
                r = map[i][j]
                count_c = 1

    return max(max_c, max_r)

def Print(map):
    for i in range(N):
        print(map[i])

# 인접한 두 칸을 골라 교환
max_candy = 0
for i in range(N):
    for j in range(N):
        # 아래로 교환
        if i+1 < N:
            if map[i][j] != map[i+1][j]:
                map[i][j], map[i + 1][j] = map[i + 1][j], map[i][j]
                result = check(map)
                if result > max_candy:
                    max_candy = result
                map[i][j], map[i + 1][j] = map[i + 1][j], map[i][j]

        if j+1 < N:
            if map[i][j] != map[i][j+1]:
                map[i][j], map[i][j + 1] = map[i][j + 1], map[i][j]
                result = check(map)
                if result > max_candy:
                    max_candy = result
                map[i][j], map[i][j + 1] = map[i][j + 1], map[i][j]

print(max_candy)