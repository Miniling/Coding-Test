# 적절한 괄호로 식의 값을 최소로 만드는 프로그램
# 처음과 마지막은 숫자(시작이 음수는 아님)
# '-'를 기준으로 수를 분리하여, 첫 수에서 나머지 숫자들을 뺄셈

PLUS = '+'
MINUS = '-'

func = input().split(MINUS)

ans = 0
for num in func[0].split(PLUS):
    ans += int(num)

for num1 in func[1:]:
    for num2 in num1.split(PLUS):
        ans -= int(num2)

print(ans)