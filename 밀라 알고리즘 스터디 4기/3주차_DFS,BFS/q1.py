# 백준 1260번. DFS와 BFS

"""
- DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램 작성
- 그래프는 양방향
- 더 이상 방문할 수 있는 점이 없는 경우 종료
- **단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문 → 정렬**
---
- N : 정점의 개수
- M : 간선의 개수
- V : 탐색을 시작할 정점의 번호
---
- 1 ≤ N ≤ 1,000
- 1 ≤ M ≤ 10,000
---
- 첫째 줄에 DFS 결과, 둘째 줄에 BFS 결과 출력
- 결과란, V부터 방문한 점을 순서대로 출력

1. 정점 개수 N, 간선 개수 M, 출발 정점 번호 V 입력 받기
2. M개의 정점 연결 정보로 그래프 구현
    1. N+1 사이즈인 배열 생성
    2. 2차원 배열로, 각 노드에 연결된 노드 정보 저장
3. **방문 순서를 지정하기 위해 그래프 내부 정렬**
4. DFS
    1. 구현 → 재귀 or 스택
    2. 방문 순서 출력
5. BFS
    1. 구현 → 큐
    2. 방문 순서 출력
"""

from sys import stdin
from collections import deque
input = stdin.readline

# 재귀로 구현한 dfs
def dfs_recursion(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs_recursion(graph, i, visited)

# 스택으로 구현한 dfs
def dfs_stack(graph, start):
    visited = [False] * len(graph)
    stack = deque([start])

    while stack:
        v = stack.pop()
        if not visited[v]:
            # 방문 후 경로에 추가, 방문 여부 변경
            visited[v] = True
            print(v, end=' ')
            # 연결된 노드를 스택에 역순으로 push
            for neighbor in reversed(graph[v]):
                if not visited[neighbor]:
                    stack.append(neighbor)

# 큐로 구현한 bfs
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v not in visited:
            # 방문 후 경로에 추가, 방문한 노드로 추가
            visited.add(v)
            print(v, end=' ')
            # 연결된 노드를 큐에 삽입
            for neighbor in graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)

def solution():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        graph[ed].append(st)
    
    for g in graph:
        g.sort()

    # visited = [False] * (N+1)
    # dfs_recursion(graph, V, visited)
    dfs_stack(graph, V)
    print()
    bfs(graph, V)
    

if __name__ == "__main__":
    solution()