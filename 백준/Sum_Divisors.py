# f(A) = A의 모든 약수를 더한 값
# x보다 작거나 같은 자연수 y의 f(y)를 더한 값은 g(x)
# ex) x=3, g(3) = f(1)+f(2)+f(3) = 1+(1+2)+(1+3) = 8

# # 자연수 N
# N = int(input())
# gn = 0
# # 1부터 N까지
# for i in range(1, N+1):
#     # i의 모든 약수 합
#     fn = 0
#     for j in range(1, i+1):
#         if(i%j == 0):
#             fn += j
#     gn += fn
#
# print(gn)

# 시간 복잡도: O(N^2) => 시간(0.5초) 초과
# hint: 약수의 반대는 배수
# ex) N까지 1의 배수는 N개, N까지 2의 배수는 N/2개, ...
N = int(input())
gn = 0
# 1부터 N까지
for i in range(1, N+1):
    count = int(N/i)
    fn = count*i
    gn += fn

print(gn)