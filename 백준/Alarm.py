# 현재 설정한 알람시간 H시 M분
# 0:0(자정), 23:59(다음날 자정 1분 전)
H, M = map(int, input().split())

if M<45:
    if H==0:
        H = 23
    else:
        H -= 1

    M = M+15
else:
    M -= 45

print(H, M)