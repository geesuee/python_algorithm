# 백준 10816번 숫자 카드 2

"""
- 숫자 카드 N개를 가지고 있음
- 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 확인
---
- N : 가지고 있는 카드 개수
- M : 개수를 확인할 숫자 개수
---
- 1 ≤ N ≤ 500,000
- 1 ≤ M ≤ 500,000
- -10,000,000 ≤ M개 내부 원소 ≤ 10,000,000

1. 가지고 있는 카드 개수 N 입력 받기
2. 가지고 있는 숫자 카드 입력 받기
3. 개수를 확인할 숫자 카드 개수 M 입력 받기
4. 개수를 확인할 숫자 입력 받기
5. Counter() 함수로 가지고 있는 숫자 카드 원소별 개수 확인
6. 확인해야할 숫자 카드 반복문 실행
    1. Counter() 결과에서 원소 개수 조회
    2. 없는 원소 조회 시 KeyError 발생하지 않고 0 반환
"""

from sys import stdin
input = stdin.readline
from collections import Counter

def solution():
    N = int(input())
    n_cards = list(map(int, input().split()))
    M = int(input())
    m_cards = list(map(int, input().split()))

    counter = Counter(n_cards)

    answer = []
    for m in m_cards:
        answer.append(str(counter[m]))
    
    print(" ".join(answer))

if __name__ == "__main__":
    solution()