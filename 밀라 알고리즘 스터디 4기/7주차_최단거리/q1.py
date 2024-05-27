# 백준 18352번. 특정 거리의 도시 찾기

"""

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