# f(A) = A의 모든 약수를 더한 값
# x보다 작거나 같은 자연수 y의 f(y)를 더한 값은 g(x)
# ex) x=3, g(3) = f(1)+f(2)+f(3) = 1+(1+2)+(1+3) = 8

# 테스트 케이스 개수 T
# T = int(input())
#
# for _ in range(T):
#     N = int(input())
#     gn = 0
#     # 1부터 N까지
#     for i in range(1, N+1):
#         # i의 모든 약수 합
#         fn = 0
#         for j in range(1, i+1):
#             if(i%j == 0):
#                 fn += j
#         gn += fn
#     print(gn)

# 시간 복잡도: T*O(N^2) => 시간(1초) 초과
# hint: 약수의 반대는 배수
# 미리 만들어두고 테스트케이스만큼 반복해서 값만 찾아서 출력
Max_N = 1000000
fn = [1] * (Max_N + 1)
gn = [0] * (Max_N + 1)

# 미리 만들어두기: 약수의 합
for i in range(2, Max_N+1):
    j = 1
    while(i*j <= Max_N):
        fn[i*j] += i
        j += 1

# 미리 만들어두기2: 현재 숫자까지의 모든 자연수의 약수 합
for i in range(1, Max_N+1):
    # 이전 숫자까지의 약수 합 + 현재 숫자의 약수 합
    gn[i] = gn[i-1] + fn[i]

T = int(input())
answer = []
# 테스트케이스만큼 반복해서 값만 찾아 출력
for _ in range(T):
    N = int(input())
    answer.append(gn[N])

print('\n'.join(map(str, answer)))

# python3가 아닌 pypy3로 제출 !!!