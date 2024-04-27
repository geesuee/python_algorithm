# 백준 2178번 미로 탐색

"""
- N x M 크기의 배열로 표현되는 미로
- 미로에서 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
    → 인접 행렬 구현
- (1, 1)에서 출발하여 (N, M)으로 이동할 때 지나야 하는 **최소 칸의 수**
    → 최단 거리 BFS, 이동 노드 개수 저장 필요
- 칸을 셀 때에는 시작 위치와 도착 위치를 모두 포함
---
- N : 배열 행 크기
- M : 배열 열 크기
---
- 2 ≤ N, M ≤ 100

1. N, M 입력 받기
2. N 줄로 입력되는 연결 정보로 그래프 생성
3. 방문 여부를 확인할 visited 배열 생성
4. BFS 구현
    1. 큐 생성
    2. 큐에 시작점 push
    3. 큐에서 하나씩 꺼내서
    4. 이동할 수 있는 상하좌우 좌표 연산, 반복문 실행
        1. 연산한 좌표가 그래프 범위 안에 있고, 방문한 적이 없는 지 확인
        2. **맞다면 visited 배열에 이전 노드의 visited 배열 값 + 1**
        3. 큐에 push
5. **N, M 까지 가는게 목적이니, visitied 에서 해당 위치 값 출력**
"""

from sys import stdin
input = stdin.readline
from collections import deque

def isOnBoard(N, M, r, c):
    return (0 <= r < N) and (0 <= c < M)

def bfs(graph, row, col, visited, N, M):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque()
    q.append((row, col))
    visited[row][col] = 1
    
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not isOnBoard(N, M, nr, nc):
                continue
            
            if (graph[nr][nc] == 1) and (visited[nr][nc] == 0):
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

def solution():
    N, M = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for i in range(N):
        line = input().rstrip()
        for j in range(len(line)):
            graph[i][j] = int(line[j])

    visited = [[0] * M for _ in range(N)]
    bfs(graph, 0, 0, visited, N, M)
    print(visited[N-1][M-1])

if __name__ == "__main__":
    solution()