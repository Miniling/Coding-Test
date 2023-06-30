import sys
input = sys.stdin.readline
x = int(input())

c, m = 1, 1
switch = 1

for i in range(x-1):
    # 1/m(홀수). 지그재그 전환
    if c==1 and m%2==1:
        m = m+1
        switch = 0
        continue
    # c(짝수)/1. 지그재그 전환
    elif c%2==0 and m==1:
        c = c+1
        switch = 1
        continue
    # c증가/m감소
    elif x>=3 and switch==0:
        c += 1
        m -= 1
        continue
    # c감소/m증가
    elif x>=3 and switch==1:
        c -= 1
        m += 1
        continue

print(str(c) + '/' + str(m))