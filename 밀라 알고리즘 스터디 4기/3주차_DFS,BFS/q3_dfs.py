# 백준 1012번 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def isOutBoard(N, M, nx, ny):
    return nx < 0 or nx >= N or ny < 0 or ny >= M

def dfs(graph, x, y):
    # 아래, 위, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if isOutBoard(len(graph), len(graph[0]), nx, ny):
            continue
        if graph[nx][ny] == 1:
            dfs(graph, nx, ny)

def solution():
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # for g in graph:
    #     print(g)
    
    baechu = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(graph, i, j)
                baechu += 1
    
    print(baechu)

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        solution()