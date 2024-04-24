# 백준 2667번 단지번호붙이기

"""
- 정사각형 모양 지도, 1은 집이 있는 곳, 0은 집이 없는 곳
    → 인접 행렬 구현
- 연결된 집 = 단지
    - 양 옆, 위 아래로 연결된 것만 연결 O
    - 대각선으로 연결된 것은 연결 X
- 총 단지 수, 단지 내 집의 수를 오름차순 정렬하여 출력
---
- N : 지도의 크기, 정사각형이기 떄문에 한 변의 길이
- 5 ≤ N ≤ 25
---
- 단지 = 연결된 그래프 집합
- 최단 거리를 찾는 문제가 아니기 때문에 DFS, BFS를 둘 다 사용 가능

1. N 입력값 받기
2. 인접 행렬 값 받아서 인접 행렬 생성
3. BFS 구현
    1. 양 옆, 위아래 노드 탐색
    2. 방문하지 않았으면 큐에 삽입
    3. 단지 내 집 수 반환(=방문 경로 내 노드 수)
4. 전체 지도를 돌면서 그래프 탐색
5. 총 단지 수 출력
6. 단지 내 집의 수 정렬 후 출력
"""

from collections import deque

def isOutBoard(N, nx, ny):
    return nx < 0 or nx >= N or ny < 0 or ny >= N

def bfs(graph, x, y, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    house = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isOutBoard(len(graph), nx, ny):
                continue
            if graph[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
                house += 1
    return house  

def solution_for_bfs():
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    
    danji = []
    visited = set()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and (i, j) not in visited:
                danji.append(bfs(graph, i, j, visited))
    
    danji.sort()
    print(len(danji))
    [print(d) for d in danji]

if __name__ == "__main__":
    solution_for_bfs()