import sys

input = sys.stdin.readline

# 1단 ~ 8단 : ascending
# 8단 ~ 1단 : descending
# else: mixed
# 1부터 8까지 숫자는 한번씩 등장

DCT = list(map(int, input().split()))
ASC = sorted(DCT)
DES = sorted(DCT, reverse=True)

print('ascending' if DCT==ASC else 'descending' if DCT==DES else 'mixed')