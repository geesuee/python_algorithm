# 백준 18352번. 특정 거리의 도시 찾기

"""
- 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재
    **→ 노드 1~N, 간선 M개, 단방향 그래프**
- 모든 도로의 거리는 1
    **→ 모든 간선의 가중치 1**
- 특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중,
최단 거리가 정확히 K인 모든 도시들의 번호 출력
    **→ BFS로 최단 거리 연산**
- 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1 출력
---
- N : 전체 노드 개수
- M : 전체 간선 개수(가중치는 모두 1)
- K : 조건으로 주어지는 최단 거리(최단 거리가 K인 노드 출력)
- X : 출발 도시
---
- 2 ≤ N ≤ 300,000
- 1 ≤ M ≤ 1,000,000
- 1 ≤ K ≤ 300,000
- 1 ≤ X ≤ N

1. N, M, K, X 입력 값 받기
2. 인접 리스트 생성
    - **최대 노드 개수가 1,000개 이상이라 인접 행렬 아닌 인접 리스트 생성**
3. 노드 간 연결 관계 인접 리스트에 추가
4. 출발 노드에서 특정 노드까지 최단 거리 저장할 배열 생성, 0으로 초기화
5. BFS로 최단 거리 연산
    1. 반복문으로 도착 노드 오름차순 접근
    2. 출발 노드로부터 BFS 연산
    3. 특정 노드에 접근할 때마다 출발 노드로부터 해당 노드까지 거리 + 1
6. 최단 거리가 K인 노드 오름차순 출력
    1. 값이 없으면 -1 출력
"""

from sys import stdin
input = stdin.readline
from collections import deque

def bfs(N, graph, start):
    distance = [0] * (N+1)
    visited = [0] * (N+1)
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        curr = queue.popleft()
        for i in graph[curr]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                distance[i] = distance[curr] + 1
    
    return distance

def solution():
    N, M, K, X = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        st, ed = map(int, input().split())
        graph[st].append(ed)
    
    distance = bfs(N, graph, X)
    
    isValid = 0
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
            isValid += 1
    
    if isValid == 0:
        print(-1)

if __name__ == "__main__":
    solution()