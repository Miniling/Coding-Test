import sys

input = sys.stdin.readline

# K개의 버튼 (1~K)
# 비밀 메뉴 조작법은 M개의 버튼 조작
# 조작법 앞뒤로 다른 조작이 섞여있어도 비밀 메뉴로 인정
# N개의 버튼 조작이 주어질 때, 비밀 메뉴 식권을 받을 수 있는지 확인.

M, N, K = map(int, input().split())

# 비밀 메뉴 조작법
recipe = list(map(int, input().split()))

# 사용자 버튼 조작
user = list(map(int, input().split()))

# 사용자 버튼 조작이 비밀 메뉴 조작법보다 짧은 경우
if N<M:
    print('normal')
else:
    secret = 0
    idx = 0
    for i in range(N):
        # 간헐적으로 맞으면 초기화
        if user[i] != recipe[idx]:
            secret = 0
            idx = 0
        # 연속으로 같을 때만 증가
        if user[i] == recipe[idx]:
            secret += 1
            idx += 1
            # 비밀 레시피가 확인됐으면 탐색 중지
            if secret == M:
                break

print('secret' if secret==M else 'normal')