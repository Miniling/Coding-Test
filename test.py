arr = [[1, 1, 4], [1, 1, 1], [4, 1, 2], [2, 2, 2]]

print(arr)
arr.sort()
print(arr)
arr.sort(key=lambda e:(e[0], -e[2]))
print(arr)