# 백준 11047번 동전 0

"""
- 준규가 가지고 있는 동전은 N 종류
- 동전을 적절히 사용해서 합을 K로 만들려고 함
- 필요한 동전 개수의 최소값
    → 동전 개수가 적으려면, 값이 큰 동전을 많이 써야함   
    → 가진 동전을 값을 기준으로 내림차순 정렬
    → 큰 가치의 동전을 최대 개수로 쓰도록하고 남는 돈 연산
---
- N : 가지고 있는 동전의 종류 수
- K : 만들어야 하는 돈의 액수
---
- 1 ≤ N ≤ 10
- 1 ≤ K ≤ 100,000,000

1. N, K 입력 값 받기
2. N개의 동전 종류 입력 값 받기
    1. 오름차순으로 주어지고, 연산은 내림차순으로 해야함
    2. 스택에 값을 받아서 하나씩 pop 하여 사용
3. 스택에 값이 있는 동안 반복문 실행
    1. 메인 프로세스
        1. 마지막에 들어간 = 가장 값이 큰 동전부터 pop
        2. K 를 만들기 위해 해당 동전이 최대 몇 개 들어갈 수 있는지 연산
        3. 위 값을 K에서 뺌
        4. 사용한 동전 개수 추가
    2. 지금 턴의 동전이 남은 값보다 크다면 → 넘어감
    3. 지금 턴의 동전으로 연산을 하고 난 값이 0 이면 → 반복문 종료
"""

from sys import stdin
input = stdin.readline
from collections import deque

def solution():
    N, K = map(int, input().split())
    
    stack = deque()
    for _ in range(N):
        stack.append(int(input()))

    used_coin = 0
    price = K
    while stack:
        coin = stack.pop()
				
		# 생각해보니 없어도 되는 부분
		# 이럴 경우 알아서 아래 연산에서 += 0, price는 그대로
        # if coin > price:
        #    continue
        
        used_coin += price // coin
        price = price % coin

        if price == 0:
            break

    print(used_coin)

if __name__ == "__main__":
    solution()