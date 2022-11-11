word = input()
answer = []

# 단어 3등분 모든 경우의 수 실행
# 처음 부터 2개 전 까지
for i in range(len(word)-2):
    # i 다음 부터 1개 전 까지
    for j in range(i+1, len(word)-1):
        # j 다음 부터 끝까지
        for k in range(j+1, len(word)):
            # 처음 부터 j까지 역순 + j부터 k까지 역순 + k부터 끝까지 역순 조합 단어 저장
            answer.append(word[:j][::-1] + word[j:k][::-1] + word[k:][::-1])

# 사전 순으로 가장 앞서는 단어 출력
print(min(answer))