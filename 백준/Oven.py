# 시작 시각과 조리에 필요한 시간을 분단위로 주어졌을 때,
# 끝나는 시각을 계산하는 프로그램
# 23시 59분에서 1분이 지나면 0시 0분

# 현재 시각
A, B = map(int, input().split())

# 필요한 시간
C = int(input())

hour = C//60
minute = C%60

B += minute
if B>=60:
    B -= 60
    A += 1

A += hour
if A>23:
    A -= 24

print(A, B)