# 백준 1238번. 파티

"""
- N 개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있음
- 어느 날 이 N 명의 학생이 X 번 마을에 모여서 파티를 벌임
- 이 마을 사이에는 총 M 개의 단방향 도로들이 있고
- i 번째 길을 지나는데 $T_i$ 의 시간을 소비함
- 각 학생들은 파티에 참석하기 위해 자신의 마을에서 X 마을까지 걸어갔다가, 다시 자신의 마을로 돌아와야 함
- 도로는 단방향이기 때문에 그들이 오고 가는 길이 다를 수도 있음
- N 명의 학생들이 다들 최단 거리로 오고 가려고 할 때,
오고 가는데 가장 많은 시간을 소비하는 학생이 누구일지 구해야 함
---
<aside>
💡 **문제 설명에서 알 수 있는 조건**

- N 개 노드, M 개 간선으로 이루어진 그래프
- 단방향 그래프
- 각 노드 간 간선은 최대 1 개
- 간선별로 가중치가 각각 다른 그래프
- 필요한 연산
    - 모든 점에서 X 지점까지 가는 최단 거리 연산 필요
    - X 지점에서 모든 점까지 가는 최단 거리 연산 필요
    - 학생별로 두 값을 더해서 최대 값 탐색 
    **~~→ 모든 노드 사이의 최단 경로를 찾을 때는 플로이드-와샬~~ → 시간 초과 💥**
    **→ 특정 노드에서 다른 모든 노드까지 최단 거리 찾을 때는 다익스트라**
</aside>
---
- 1 ≤ N ≤ 1,000
- 1 ≤ M ≤ 10,000
- 1 ≤ $T_i$ ≤ 100 
    **→ 노드 개수가 최대 1,000 건이니 인접 리스트로 구현**
    *(인접 행렬이의 장점은 구현이 간단하다 정도라.. 앞으로는 그냥 다 인접 리스트로 구현할까 싶음)*
    **→ 플로이드-와샬 시간 복잡도 O($N^3$), 이 문제에서 최대 O($10^9$) < 1초($10^{10}$) 아슬아슬,,💥**
    **→ 다익스트라 시간 복잡도 $O((N+M)logN))$, 이 문제에서 각 노드별로 다익스트라 두 번 수행
    이 문제에서 $O(2N*(N+M)log N)$, 최대 $O(6*10^7)$ > $O(10^8)$ < 1초($10^{10}$)**
---
- 시간 제한 1 초
- 메모리 제한 128 MB
"""

from sys import stdin
input = stdin.readline
import heapq

# 플로이드-와샬 풀이 -> 시간 초과
def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf')] * (V+1) for _ in range(V+1)]

    for i in range(1, V+1):
        dist[i][i] = 0
    
    for i in range(1, V+1):
        for v, weight in graph[i]:
            dist[i][v] = weight

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# 다익스트라 풀이
def dijkstra(graph, start):
    q = [(0, start)]
    dist = {node:float('inf') for node in graph}
    dist[start] = 0

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        if dist[curr_node] < curr_dist:
            continue

        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(q, (new_dist, neighbor))
    
    return dist

def solution():
    N, M, X = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}

    for _ in range(M):
        st, ed, w = map(int, input().split())
        graph[st].append((ed, w))

    max_w = -1
    for student in range(1, N+1):
        go = dijkstra(graph, student)
        back = dijkstra(graph, X)
        total_w = go[X] + back[student]
        max_w = max(max_w, total_w)

    print(max_w)

if __name__ == "__main__":
    solution()