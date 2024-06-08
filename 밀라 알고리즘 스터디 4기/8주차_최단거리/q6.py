# 백준 1162번. 도로 포장

"""
- 준영이는 매일 서울에서 포천까지 출퇴근을 함
- N 개의 도시가 있고, 그 사이 도로와 도로를 통과할 때 걸리는 시간이 주어짐
- 최소 시간이 걸리도록하는 K 개 이하의 도로를 포장하려 함
- 포장하게 되면 도로를 지나는데 걸리는 시간이 0이 됨
- 서울은 1 번 도시, 포천은 N 번 도시로 정함
- 도로는 양방향 도로임
---
<aside>
💡 **문제 설명에서 알 수 있는 조건**
- N 개 노드, M 개 간선으로 이루어진 그래프
- 양방향 그래프
- 간선별로 가중치가 각각 다른 그래프
- 필요한 연산
    - 1 번 노드에서 N 번 노드까지 가는데 걸리는 최단 거리 연산
    - 경로 중 K 개를 포장하면, 가중치가 0 이 됨, 이 과정을 거친 후 최단 거리 연산
</aside>
---
- N : 도시의 수 = 노드 개수
- M : 도로의 수 = 간선 개수
- K : 포장할 도로의 수
- $w_i$  : 각 도로를 통과하는데 걸리는 시간 = 가중치
---
- 1 ≤ N ≤ 10,000
- 1 ≤ M ≤ 50,000
- 1 ≤ K ≤ 20
- 1 ≤ $w_i$ ≤ 1,000,000
---
- 시간 제한 2 초
- 메모리 제한 128 MB
"""

# 내 풀이 > 틀림
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def find_all_paths_with_weights(graph, start, end, path=[], weights=[]):
    path = path + [start]
    if start == end:
        return [(path, weights)]
    if start not in graph:
        return []
    paths = []

    for node, weight in graph[start]:
        if node not in path:
            new_paths = find_all_paths_with_weights(graph, node, end, path, weights+[weight])
            for p in new_paths:
                paths.append(p)
    return paths

def solution():
    N, M, K = map(int, input().split())
    graph = {node:[] for node in range(1, N+1)}

    for _ in range(M):
        st, ed, w = map(int, input().split())
        graph[st].append((ed, w))
        graph[ed].append((st, w))
    
    paths = find_all_paths_with_weights(graph, 1, N)
    
    min_w = float('inf')
    for p, w in paths:
        sorted_w = sorted(w, reverse=True)
        if len(sorted_w) >= K:
            final_w_sum = sum(sorted_w[K:])
        else:
            final_w_sum = 0
        
        if final_w_sum < min_w:
            min_w = final_w_sum
    
    print(min_w)


if __name__ == "__main__":
    solution()