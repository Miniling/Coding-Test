# 00:00 ~ 24:00 사이 근무시간(근무 외 시간을 제외하지 않음)

import sys

input = sys.stdin.readline

working = 0
# 5일 출근 => 5회 반복
for _ in range(5):
    start, end = map(str, input().split())
    working += (int(end[:2])-int(start[:2]))*60 + int(end[3:])-int(start[3:])

print(working)