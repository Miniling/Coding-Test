#  1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

while(True):
    try:
        # 정수 n 입력
        N = int(input())
    except:
        break

    num = 1
    length = 1
    while(True):
        remain = num%N
        if(remain == 0):
            print(length)
            break
        # 1로만 이루어진 정수 생성
        num = num*10+1
        # 자릿수 증가
        length += 1