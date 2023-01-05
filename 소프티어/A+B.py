import sys

# 표준 입력을 'input'이라는 이름으로 사용.
input = sys.stdin.readline

# 내장 함수인 input()과는 다른 input()
T = int(input())

for i in range(T):
    A, B = map(int, input().split())

    print("Case #%d:"%(i+1), (A+B)) # %d == %변수