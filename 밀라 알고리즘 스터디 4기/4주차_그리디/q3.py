# 백준 12845번 모두의 마블

"""
- 순서가 매겨진 여러 장의 카드가 있다.
- 각각의 카드는 저마다 레벨이 있다.
- 카드 A에 카드 B를 덧붙일 수 있다.
    - **두 카드는 인접한 카드여야 한다.**
    - **업그레이드 된 카드 A의 레벨은 변하지 않는다.**
    - 카드를 합성하면, 이전 카드는 없어지고 결과 카드만 남는다.
- 카드 합성을 할 때마다 두 카드의 레벨의 합만큼 골드를 받는다.
    **→ 레벨이 높은 카드부터 합성을 해야겠다.**
    **→ 레벨 순으로 정렬 후, 큰 값부터 인접한 카드와 합성해야겠다.**
- 영관이가 골드를 최대한 많이 받을 수 있게 해야 한다.
---
- n : 카드의 개수
- L : 카드의 레벨
---
- 1 ≤ n ≤ 1,000
- 0 < L ≤ 100,000

1. 카드의 개수 n 입력 받기
2. 각 카드 레벨 값 입력 받기
3. 레벨을 기준으로 ~~내림차순 정렬~~ → heapify
4. 더 이상 카드 합성을 못할 때까지 반복
    1. 맨 앞에 있는 가장 큰 값과, 그 뒤의 인접한 값을 합성
    2. 두 카드의 레벨의 합으로 받게될 골드 값 연산
    3. 합성한 카드는 배열에서 삭제하고, 새로 합성된 카드를 배열에 추가
    **→ 정렬하고, 값을 뺐다 넣었다 하는 부분이 있으니까 heapq를 사용해보자**
    - 합성된 카드 레벨은 합성한 카드 중 큰 레벨과 동일하기 때문에 다시 맨 앞에 넣어주어도 정렬이 유지되어 단순 배열, 큐로 풀어도 가능하지만
    - 매번 정렬이 필요한 경우라면 heapq로 관리하는 것이 시간복잡도가 더 낮음
5. 받은 골드 값 출력
"""

from sys import stdin
input = stdin.readline
import heapq
from collections import deque

# 힙 풀이
def solution_heap():
    n = int(input())
    levels = list(map(int, input().split()))
    levels = [-x for x in levels]

    heapq.heapify(levels)

    gold = 0
    while len(levels) > 1:
        a = -heapq.heappop(levels)
        b = -heapq.heappop(levels)
        gold += a + b
        heapq.heappush(levels, -a)

    print(gold)

# 배열 풀이
def solution_arr():
    n = int(input())
    levels = list(map(int, input().split()))
    q = deque(sorted(levels, reverse=True))

    gold = 0
    while len(q) > 1:
        a = q.popleft()
        b = q.popleft()
        gold += a + b
        q.appendleft(a)

    print(gold)

if __name__ == "__main__":
    solution_heap()
    solution_arr()