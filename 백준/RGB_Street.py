n = int(input())

RGB_price = []
max_ = 1000
total = 0
idx = 0
for i in range(n):
    RGB_price.append(list(map(int, input().split(' '))))

    # 두번 째 부터는 직전과 중복되지 않는 작은 값 저장
    if i > 0:
        RGB_price[i][idx] = max_

    price = min(RGB_price[i])
    total += price
    idx = RGB_price[i].index(price)

    print(RGB_price[i], price, idx)

print(total)