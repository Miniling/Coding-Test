import sys

name = list(input())
abb = []

A = ord('A')
Z = ord('Z')

# 대문자 ASCII값 범위를 지정하여 대문자에 해당하면 뽑아냄
for i in range(len(name)):
    if(ord(name[i]) >= A and ord(name[i]) <= Z):
        abb.append(name[i])

# 배열을 순환하면서 요소 사이에 ''를 포함한 문자열 반환
logo = ''.join(s for s in abb)
print(logo)
