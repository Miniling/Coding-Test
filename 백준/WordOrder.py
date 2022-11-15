n = int(input())
words = []

# 튜플에 (단어, 길이) 저장
for i in range(n):
    word = input()
    words.append((word, len(word)))

# 길이, 사전순 정렬
words.sort(key=lambda e: (e[1], e[0]))

result = []
idx = 0
result.append(words[0][0])
# 중복 제거 필터링
for i in range(1, n):
    word = words[i][0]
    if(word != result[idx]):
        result.append(word)
        idx += 1

# 정렬, 필터링된 단어 출력
for i in range(len(result)):
    print(result[i])
