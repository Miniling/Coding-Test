import sys
input = sys.stdin.readline

n = sorted(list(input()), reverse=True)

answer = ''

for i in n:
    answer += i

print(answer)