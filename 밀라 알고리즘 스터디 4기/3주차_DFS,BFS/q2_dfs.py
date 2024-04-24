# 백준 2667번 단지번호붙이기

import sys
sys.setrecursionlimit(10**6) # 재귀 최대 깊이 설정

def isOutBoard(N, nx, ny):
    return nx < 0 or nx >= N or ny < 0 or ny >= N

def dfs(graph, x, y, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited.add((x, y))
    house = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isOutBoard(len(graph), nx, ny):
            continue
        if graph[nx][ny] == 1 and (nx, ny) not in visited:
            house += dfs(graph, nx, ny, visited)
    
    return house

def solution_for_dfs():
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    
    danji = []
    visited = set()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and (i, j) not in visited:
                danji.append(dfs(graph, i, j, visited))
    
    danji.sort()
    print(len(danji))
    [print(d) for d in danji]

if __name__ == "__main__":
    solution_for_dfs()