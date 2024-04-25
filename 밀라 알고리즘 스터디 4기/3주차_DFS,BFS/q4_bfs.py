# 백준 11724번 연결 요소의 개수

import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start]=True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

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
            bfs(graph, v, visited)
            group += 1
    
    print(group)

if __name__ == "__main__":
    solution()