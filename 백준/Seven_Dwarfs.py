# 난쟁이의 키는 변하지 않는다.
# 모든 키의 합
# 100 == 일곱 난쟁이의 키 = 합 - 포함되지 않는 두 명

# 순열 함수 라이브러리
import itertools

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

# combination(iterable, r): iterable에서 원소 개수가 r개인 모든 조합
for seven_dwarfs in itertools.combinations(dwarfs, 7):
    if sum(seven_dwarfs) == 100:
        # 튜플 형태((a, b, ...))로 출력되어서 리스트로 변형
        seven_dwarfs = list(seven_dwarfs)
        seven_dwarfs.sort()
        for tall in seven_dwarfs:
            print(tall)
        break