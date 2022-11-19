# 테스트 케이스 개수(고정)
T = 10

for test_case in range(1, T+1):
    buildings = int(input())
    heights = list(map(int, input().split()))

    answer = 0
    idx = 2

    for i in range(len(heights)-4):
        # 조망권 확보 세대 계산
        cur = heights[idx]
        far_left = heights[idx-2]
        near_left = heights[idx-1]
        near_right = heights[idx+1]
        far_right = heights[idx+2]

        view_left = min(cur-far_left, cur-near_left)
        view_right = min(cur-far_right, cur-near_right)

        # 좌우 2칸 이내 높이 차의 최솟값 = 조망권 세대 수
        view = min(view_left, view_right)

        if(view > 0):
            answer += view

        idx += 1

    # 결과 출력
    print('#'+str(test_case)+' '+str(answer))