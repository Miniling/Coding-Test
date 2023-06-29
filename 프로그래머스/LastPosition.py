v = []
answer = []

for i in range(3):
    xy = list(map(int, input().split(' ')))
    v.append(xy)

x, y = [], []

for point in v:
    # x좌표가 없으면 등록, 있으면 제거(중복 위치 제거)
    if point[0] not in x:
        x.append(point[0])
    elif point[0] in x:
        x.remove(point[0])

    # y좌표가 없으면 등록, 있으면 제거(중복 위치 제거)
    if point[1] not in y:
        y.append(point[1])
    elif point[1] in y:
        y.remove(point[1])

# 남은 x, y를 마지막 좌표로 등록
answer = x + y

print(answer)