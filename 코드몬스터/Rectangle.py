def countPos(Pos):
    # 첫 번째 좌표와 개수 설정
    posA, countA = Pos[0], 1
    posB, countB = 0, 0
    for i in range(1, len(Pos)):
        if(Pos[i] == posA):
            countA += 1
        else:
            posB = pos[i]
            countB += 1

    if(countA < countB):
        return posA
    else:
        return  posB

def solution(v):
    answer = []

    # x, y좌표 추출
    xPos, yPos = [], []
    for i in range(len(v)):
        xPos.append(v[i][0])
        yPos.append(v[i][1])

    # 개수 확인
    x = countPos(xPos)
    y = countPos(yPos)

    # 개수가 적은 좌표 정답으로 제출
    answer.append(x)
    answer.append(y)

    return answer