# 백준 5972번. 택배 배송

"""
- 농부 현서는 농부 찬홍이에게 택배를 배달
- 평화롭게 가려면 가는 길에 만나는 모든 소들에게 맛있는 여물을 줘야 함
- 최소한의 소들을 만나면서 지나가고 싶음
- 지도에는 N개의 헛간(=노드), M개의 양방향 소들의 길(=간선)이 있음
- 각 길에는 $C_i$ 마리의 소가 있음(=간선 가중치)
- 두 개의 헛간은 하나 이상의 길로 연결되어 있을 수 있음
- 길은 양방향으로 연결되어 있음
- 농부 현서는 헛간 1에 있고, 농부 찬홍이는 헛간 N에 있음
    **→ 현서에서부터 찬홍이까지 간선 가중치를 고려한 최단 거리 연산**
    **→ 음의 가중치가 없는 그래프, 가중치가 각각 다른 상황에서 최단 거리 연산 = 다익스트라**
---
- N : 헛간 개수 = 노드 개수
- M : 길의 수 = 간선 개수
- C_i : 길에 있는 소의 수 = 간선 가중치
---
- 1 ≤ N ≤ 50,000
- 1 ≤ M ≤ 50,000
- 0 ≤ $C_i$ ≤ 1,000 
    **→ 노드 개수와 간선 개수가 많아서 인접 리스트로 그래프 구현**
---
- 시간 제한 1초
- 메모리 제한 128 MB

1. 노드 개수 N, 간선 개수 M 입력 받기
2. M개 만큼 간선 정보 입력 받아 그래프 생성(시작 노드, 끝 노드, 가중치)
    1. 인접 리스트로 구현
3. 다익스트라로 현서가 있는 1번 노드에서 모든 노드에 대한 최단 거리 연산
4. 결과 배열 내 N 번 노드까지 최단 거리 출력
"""

from sys import stdin
input = stdin.readline
import heapq

def dijkstra(graph, start, N):
    q = [(0, start)]
    visited = [False] * (N + 1)
    distances = {node: float('inf') for node in range(1, N + 1)}
    distances[start] = 0

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        if visited[curr_node]:
            continue

        visited[curr_node] = True

        for neighbor, w in graph[curr_node]:
            new_dist = curr_dist + w
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(q, (new_dist, neighbor))
    
    return distances

def solution():
    N, M = map(int, input().split())

    graph = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        st, ed, w = map(int, input().split())
        graph[st].append((ed, w))
        graph[ed].append((st, w))
    
    result = dijkstra(graph, 1, N)
    print(result[N])

if __name__ == "__main__":
    solution()