def howMuch(seasoning, fried, banban, sNeed, fNeed):
    # 반반 2개 가격이 더 비싼 경우, 그대로 계산
    if (banban * 2) > (seasoning + fried):
        return (seasoning * sNeed) + (fried * fNeed)
    # 반반 2개 가격이 더 싼 경우, 반반*2*최소 + 남은 치킨 중 반반2개와 비교해서 더 싼 가격
    else:
        return (banban * 2 * min(sNeed, fNeed) + min(seasoning, banban * 2) * max(0, sNeed - fNeed) + min(fried, banban * 2) * max(0, fNeed - sNeed))

seasoning, fried, banban, sNeed, fNeed = map(int, input().split())
print(howMuch(seasoning, fried, banban, sNeed, fNeed))
