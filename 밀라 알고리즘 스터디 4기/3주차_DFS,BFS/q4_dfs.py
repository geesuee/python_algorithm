# 백준 11724번 연결 요소의 개수

"""
- 방향 없는 그래프    
    → 두 노드 간 연결 정보가 나오면 양쪽으로 연결 해주어야 함 
- 연결 요소 (Connected Component)의 개수를 구하라
    → DFS/BFS 모두 사용할 수 있고, 방문 경로를 반환할 필요 없으니 DFS 구현이 더 쉬움
---
- N : 정점의 개수
- M : 간선의 개수
---
- 1 ≤ N ≤ 1,000
- 0 ≤ M ≤ N×(N-1)/2 
    → 정점의 개수가 1000개 이하일 때까지는 인접 행렬 구현 추천(구현 난이도가 낮으니까!)
    → 제한 시간이 3초라서 O(N^4) 가 나와도 시간 제한에 걸리지는 않겠지만, 정점의 개수가 많아질 경우 인접 행렬은 메모리 낭비도 많음
    → 이번 문제는 인접 리스트로 구현💪

1. 정점의 개수 N, 간선의 개수 M 입력 받기
2. 정점이 N개인 인접 리스트 그래프 생성
3. 연결 정보 입력 받아 그래프 갱신
4. 방문 여부 boolean을 담을 visited 배열 생성
5. 정점을 하나씩 돌면서 DFS 실행
6. 한 뭉텅이가 다 돌아가면 연결 요소 개수 + 1
7. 연결 요소 개수 출력
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    group = 0
    visited = [False] * (N+1)
    for v in range(1, N+1):
        if not visited[v]:
            dfs(graph, v, visited)
            group += 1
    
    print(group)

if __name__ == "__main__":
    solution()