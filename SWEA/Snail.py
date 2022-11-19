test = int(input())
case = []

# 입력
for i in range(test):
    case.append(int(input()))

def checkMap(map):
    completed = 0
    for i in range(len(map)):
        if(0 not in map[i]):
            completed += 1
    return completed

# Snail 계산
def makeSnail(map):
    y, x = 0, 1
    count = 1
    max_line = len(map)
    min_line = -1

    while(checkMap(map) < len(map)):
        # → 방향
        if(count == 1):
            map[y][x] = map[y][x-1] + 1
            x += 1
            if(x == max_line):
                x -= 1
                y += 1
                count = 2
        # ↓ 방향
        elif(count == 2):
            map[y][x] = map[y-1][x] + 1
            y += 1
            if(y == max_line):
                y -= 1
                x -= 1
                count = 3
                max_line -= 1
        # ← 방향
        elif(count == 3):
            map[y][x] = map[y][x+1] + 1
            x -= 1
            if(x == min_line):
                x += 1
                y -= 1
                count = 4
                min_line += 1
        # ↑ 방향
        elif(count == 4):
            map[y][x] = map[y+1][x] + 1
            y -= 1
            if(y == min_line):
                y += 1
                x += 1
                count = 1

    return map

def makeMap(size):
    map = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        map.append(line)

    map[0][0] = 1
    snail = makeSnail(map)

    for i in range(size):
        for j in range(size):
            print(snail[i][j], end=' ')
        print('')

# 결과 출력
for i in range(test):
    print('#'+str(i+1))
    makeMap(case[i])