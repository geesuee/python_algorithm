# 백준 1697번 숨바꼭질

"""
- 수빈이는 점 N 에 있고
- 동생은 점 K 에 있음
- 수빈이가
    - 걸으면 1초 후에 X-1, X+1 로 이동
    - 순간 이동하면 1초 후에 2*X 위치로 이동
- 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 연산
    **→ 수빈이가 동생을 찾는 최단 거리 연산 = BFS 구현**
---
- N : 수빈이의 위치
- K : 동생의 위치
---
- 0 ≤ N ≤ 100,000
- 0 ≤ K ≤ 100,000

1. N, K 입력 값 받기
2. BFS 구현
    1. 큐 생성, 초기 값 push 
    2. 큐에 값이 있는 것을 조건으로 while 문 실행
        1. popleft 한 값이 동생의 위치면 반복문 종료
        2. 1초에 수빈이가 움직일 수 있는 동선 연산 (X-1, X+1, 2*X)
        3. **범위 내에 속하고, 방문하지 않은 지점이면**
            1. **해당 지점까지 오는데 경유한 지점 개수를 배열에 저장**
            2. 큐에 push
"""

from sys import stdin
input = stdin.readline
from collections import deque

def bfs(N, K, arr):
    q = deque()
    q.append(N)

    while q:
        v = q.popleft()
        # 동생을 찾으면 종료
        if v == K:
            return arr[v]

        # 이동할 수 있는 자리 연산
        for nv in (v-1, v+1, 2*v):
            if 0 <= nv < 100001 and not arr[nv]:
                # 여기까지 오기 위해 몇 개의 노드를 거쳤는지 저장
                arr[nv] = arr[v] + 1
                q.append(nv)

def solution():
    N, K = map(int, input().split())

    arr = [0] * 100001
    print(bfs(N, K, arr))

if __name__ == "__main__":
    solution()