# 각 계란에는 내구도와 무게가 존재
# 계란으로 계란을 치면 내구도는 상대 계란의 무게만큼 깎임
# 내구도가 0 이하가 되면 깨진다

# 계란 수
n = int(input())

# 내구도, 무게
eggs = []
for _ in range(n):
    eggs.append(list(map(int, input().split())))

