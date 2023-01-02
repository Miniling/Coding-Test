# 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램
# 대,소문자 구분 X
# hint: 한 문자의 대,소문자 아스키값 차이는 32
# A:65 ~ Z:90
# a:97 ~ z:122

word = list(input())

# 대문자로 변환
for i in range(len(word)):
    if ord(word[i])>90:
        word[i] = chr(ord(word[i])-32)
word.sort()

# 단어에 나온 알파벳과 개수 정리
table_word = []
table_count = []
idx = -1
for w in word:
    # 새로운 알파벳 추가
    if w not in table_word:
        table_word.append(w)
        table_count.append(1)
        idx += 1
    # 존재하는 알파벳
    else:
        table_count[idx] += 1

maximum = max(table_count)
ans = []
for i in range(len(table_count)):
    if table_count[i]==maximum:
        ans.append(table_word[i])

if len(ans)>1:
    print('?')
else:
    print(ans[0])