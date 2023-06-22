n, m = map(int, input().split(' '))
hear = set()
see = set()

for i in range(n):
    hear.add(input())

for i in range(m):
    see.add(input())

nolist = sorted(list(hear&see))
print(len(nolist))
for name in nolist:
    print(name)