# CodingTest

<h2>ToDo.</h2>
📝 매일 최소 한 문제씩 풀기 !
<br>
<p style="font-weight: bold"><학습노트 ✏></p>
<a>[[ 백준 ]]</a> <br>
1. 자동차 번호판: Python  ord('문자') => 문자의 ASCII값 반환  <br>
2. 반반치킨: 문제의 '요구사항' 확인!!!   <br>
3. 단어 분리하기: list[A:B:C] => A부터 B까지 C개씩 받기(공백이면 처음(끝)까지, C 음수면 역순)   <br>
4. 나머지 연산: (A*B)%N == ((A%N) * (B%N))%N. ex) 111%N == (11*10+1)%N == ((11%N) * 10 + 1)%N   <br>
5. 소수 찾기: 에라토스테네스의 체. N까지의 값이 저장된 배열에서 소수의 배수를 전부 지우는 방식 => 시간 복잡도 < 루트N   <br>
6. 일곱 난쟁이: # 순열 함수 라이브러리(import itertools). combination(iterable, r): iterable에서 원소 개수가 r개인 모든 조합   <br>
7. 사탕 게임: 오른쪽+아래만 검산해도 4방향을 모두 확인할 수 있다!   <br>
8. 로또: 6번 일곱 난쟁이와 동일. N개 중 a개를 고르는 모든 경우의 수를 출력하는 for tuple in itertools.combination(list, count)   <br>
<br><br>
<a>[[ 소프티어 ]]</a> <br>
1. 징검다리: 예외처리는 맨 마지막에 고려. 문제 분석 및 기능 계획 후 작성!!! <br>
2. 약자: ''.join(s for s in 리스트) => 배열을 문자열로 변환 ('문자'.join : 요소 사이에 '문자' 추가)  <br>
3. 이중 큐: [v, ...].sort() / [v, ...].sort(reverse=True) => 오름 / 내림차순 정렬, <br>
            [('key', value), ...].sort(key = lambda e: e[1]) => value기준 오름차순 정렬  <br>
            [('key', value), ...].sort(key = lambda e: (e[0], -e[1])) => 'key' 오름차순, value 내림차순 정렬  <br>
<br>

<h3>※잊지말고 기억해서 또 실수하지 않기!!!</h3>
list.sort(key=lambda e: (e[0], -e[2])) => 리스트 (0번째 요소 오름차순 -> 2번째 요소 내림차순) 정렬  <br>
import sys, input=sys.stdin.readline  => input() 내장함수 대신 줄 단위 읽기로 input 변환하여 사용.(시간 단축)  <br>
