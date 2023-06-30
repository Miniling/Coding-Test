# import itertools
import math
import sys
input = sys.stdin.readline
T = int(input())

for case in range(T):
    n, m = map(int, input().split(' '))
    answer = 0

    # 수동 계산, 시간 초과!
    # east = [0]*m

    # for bridge in itertools.combinations(east, n):
    #     answer += 1

    answer = math.factorial(m) // (math.factorial(n)*math.factorial(m-n))

    print(answer)