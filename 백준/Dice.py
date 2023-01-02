# 주사위 3개
# 같은 눈 3개: 10,000원+(같은 눈)x1,000원
# 같은 눈 2개: 1,000원+(같은 눈)x100원
# 모두 다른 눈: (가장 큰 눈)x100원

# 중복 확인 란
numbers = [0]*7

num1, num2, num3 = map(int, input().split())
numbers[num1] += 1
numbers[num2] += 1
numbers[num3] += 1

price = 0
result = max(numbers)
if result == 3:
    price = 10000+(num1*1000)
else:
    for i in range(len(numbers)):
        if numbers[i] == 2:
            price = 1000+(i*100)
            break
        elif numbers[i] == 1:
            price = i*100

print(price)