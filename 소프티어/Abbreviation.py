import sys

name = list(input())
abb = []

A = ord('A')
Z = ord('Z')

for i in range(len(name)):
    if(ord(name[i]) >= A and ord(name[i]) <= Z):
        abb.append(name[i])

logo = ''.join(s for s in abb)
print(logo)
