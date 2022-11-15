# def solution(n, roads, sources, destination):
n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5

answer = []

# 목적지까지 최소 이동 횟수
def moveRoad(current, destination, moved):
    count = -1
    for i in range(len(roads)):
        if ((current in roads[i]) and (destination in roads[i])):
            return 1
        elif ((current in roads[i]) and ((current in moved) == False)):
            moved.append(current)
            print('이동 경로', moved)
            idx = roads[i].index(current) + 1
            go = int(len(roads[i]) / idx) - 1
            go = roads[i][go]
            arrive = moveRoad(go, destination, moved)
            if(arrive == 1):
                count = arrive + 1

    return count

# 탈출 인원수만큼 반복
for i in range(len(sources)):
    moved = []
    # 현재 위치가 목적지라면 이동X
    current = sources[i]
    if (current == destination):
        answer.append(0)
    else:
        move = moveRoad(current, destination, moved)
        answer.append(move)

print(answer)