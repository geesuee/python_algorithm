# 백준 1012번 유기농 배추

"""
- 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
    → 상하좌우 좌표 이동 구현
- 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사
    → 전체 보드 위에 몇 개의 그래프가 있는지 DFS/BFS 탐색
---
- T : 테스트 케이스 개수
- M : 배추를 심은 배추 밭의 가로 길이
- N : 배추를 심은 배추 밭의 세로 길이
- K : 배추가 심어져 있는 위치 개수
- X, Y : 배추가 심어진 위치 좌표
---
- 1 ≤ M ≤ 50
- 1 ≤ N ≤ 50

1. 테스트 케이스 개수 T 입력 받기
2. 테스트 케이스별 반복문 실행
---
반복문 내부
1. 가로 길이 M, 세로 길이 N, 배추 개수 K 입력 받기
    세로 길이(Y) = 행 개수, 가로 길이(M) = 열 개수
2. [[0 * M] for _ in range(N)] 형태 배추 밭 만들기
3. K개 입력 값 받아서 배추가 있는 좌표 값 1로 변경
    M과 관련된 X 값은 열 값 
    N과 관련된 Y 값은 행 값
    **→ X, Y 뒤 바꿔서 배추 좌표 값 넣기**
4. 전체 배추밭을 돌면서 DFS/BFS 실행
5. 한 번 탐색이 끝날 때 마다 배추 모임 값 +1
6. 배추 모임 출력
"""

from sys import stdin
input = stdin.readline
from collections import deque

def isOutBoard(N, M, nx, ny):
    return nx < 0 or nx >= N or ny < 0 or ny >= M

def bfs(graph, x, y):
    # 아래, 위, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isOutBoard(len(graph), len(graph[0]), nx, ny):
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

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
                bfs(graph, i, j)
                baechu += 1
    
    print(baechu)

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        solution()