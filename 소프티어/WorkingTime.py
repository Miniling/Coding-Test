# 00:00 ~ 24:00 사이 근무시간(근무 외 시간을 제외하지 않음)

import sys

input = sys.stdin.readline

work_h, work_m = 0, 0
# 5일 출근 => 5회 반복
for _ in range(5):
    start, end = map(str, input().split())
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    work_h += (end_h-start_h)
    work_m += (end_m-start_m)

print(work_h*60+work_m)