# 주어진 수 N개
N = int(input())
numbers = list(map(int, input().split()))

# 에라토스테네스의 체
max_num = max(numbers)
check = [0]*(max_num+1)
check[0] = check[1] = True

for i in range(2, max_num+1):
    if not check[i]:
        j = i+i
        while j <= max_num:
            check[j] = True
            j += i

count = 0
for i in range(0, max_num+1):
    if (i in numbers)and(check[i] == False):
        count += 1

print(count)