# 백준 14940번. 쉬운 최단거리

"""
- 지도가 주어지면 모든 지점에 대해서 목표 지점까지 거리를 구해야 함
    **→ 모든 지점에서 목표 지점까지 거리 = 목표 지점에서 모든 지점까지 거리**
    **→ ~~다익스트라~~** 다익스트라로도 풀 수는 있겠지만, 다익스트라는 이동 가중치가 다를 때 더 유리
- 이동은 가로와 세로로만 움직일 수 있음 (=상하좌우)
    **→ 이동 할 수 있는 곳이기만 하면 이동 가능, 가중치가 다 1로 동일(=없는 것과 동일)**
    **→ BFS 사용 가능,** 그래프 가중치가 없을 때는 BFS 가 더 유리
- 지도에서
    - 0은 갈 수 없는 땅
    - 1은 갈 수 있는 땅
    - 2는 목표 지점(단 한 개)
- 각 지점에서 목표 지점까지 거리 출력
    - 원래 갈 수 없는 땅인 위치는 0 출력
    - 원래 갈 수 있지만, 목표 지점에 도달할 수 없는 위치는 -1 출력
---
- n : 지도의 세로 크기
- m : 지도의 가로 크기
---
- 2 ≤ n ≤ 1,000
- 2 ≤ m ≤ 1,000
- 제한 시간 1초 ($10^{10}$)
    → 다익스트라를
    - for 문으로 구현 시 시간 복잡도 $O(V^2)$, 여기서 최대 $(1000*1000)^2 = 10^{12}$ **→ 시간 초과 💥?**
    - **heapq 로 구현** 시 시간 복잡도 $O((V+E)logV)≈O(VlogV)$, 여기서 최대 $10^6log10^6$

> 다익스트라 풀이 설계 -> 틀림ㅜㅜ
1. 세로 크기, 즉 행의 수 n 입력 받기
2. 가로 크기, 즉 열의 수 m 입력 받기
3. 그래프 정보 입력 받기
    1. n 만큼 반복문 돌아 한 줄씩 입력 값 받고 리스트로 만들어서 리스트 안에 저장 (이차원 배열)
    2. 목표 지점인 2를 찾으면 해당 값이 몇 행, 몇 열인지 따로 변수에 저장
4. 다익스트라로 목표 지점에서부터 모든 지점까지 거리 연산
    1. heapq 로 구현
    2. 원래 갈 수 없는 땅은 0, 원래 갈 수 있지만 목표 지점에서 갈 수 없는 땅은 -1, 갈 수 있는 땅은 거리 연산
5. 위치 순서대로 목표 지점에서 해당 지점까지 거리 출력

> 간선 가중치가 다 1로 동일한 상황이기 때문에 BFS 가 더 유리
> BFS 코드 수정 중
"""

from sys import stdin
input = stdin.readline
import heapq
from collections import deque

# 다익스트라 풀이 -> 틀린 풀이
def dijkstra(graph, goal_r, goal_c):
    n = len(graph)
    m = len(graph[0])

    # 상, 하, 좌, 우 이동
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    priority_queue = [(0, goal_r, goal_c)]
    visited = [[False]*m for _ in range(n)]
    distances = [[float('inf')] * m for _ in range (n)]
    distances[goal_r][goal_c] = 0

    while priority_queue:
        curr_dist, curr_r, curr_c = heapq.heappop(priority_queue)
        # print("*** curr_dist:", curr_dist, " curr_r:", curr_r, " curr_c:", curr_c)

        if visited[curr_r][curr_c] == True:
            # print(" ㄴ 여긴 이미 방문해서 넘어감")
            continue
            
        visited[curr_r][curr_c] == True

        # 상, 하, 좌, 우 이동
        for i in range(4):
            new_r = curr_r + dr[i]
            new_c = curr_c + dc[i]
            # print("-- new_r: ", new_r, " new_c:", new_c)

            # 지도 안 여부 확인
            if (0 <= new_r <= n-1) and (0 <= new_c <= m-1) and visited[new_r][new_c] == False:
                # print("ㄴ 지도 안에 있고, 안 가봄")
                # 원래 갈 수 없는 땅
                if graph[new_r][new_c] == 0:
                    # print("ㄴ 못 가는 땅ㅜ")
                    distances[new_r][new_c] = 0
                # 원래 갈 수 있는 땅
                if graph[new_r][new_c] == 1:
                    # print("ㄴ 갈 수 있는 땅!")
                    new_distance = curr_dist + 1
                    if new_distance < distances[new_r][new_c]:
                        distances[new_r][new_c] = new_distance
                        heapq.heappush(priority_queue, (new_distance, new_r, new_c))

    # 갈 수 없어서 값이 갱신되지 않은 곳은 -1로 변경
    for i in range(n):
        for j in range(m):
            if distances[i][j] == float('inf'):
                distances[i][j] = -1

    return distances

# BFS 풀이 -> 이것도 틀린 풀이 어디가 틀렸지..?
def bfs(graph, goal_r, goal_c):
    n = len(graph)
    m = len(graph[0])

    # 상, 하, 좌, 우 이동
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 결과 배열에 초기값을 -1로 설정
    result = [[-1] * m for _ in range(n)]
    result[goal_r][goal_c] = 0

    visited = [[False]*(m) for _ in range(n)]
    visited[goal_r][goal_c] = True

    queue = deque()
    queue.append((goal_r, goal_c))

    while queue:
        curr_r, curr_c = queue.popleft()
        # print("curr_r:", curr_r, " curr_c:", curr_c)

        for i in range(4):
            new_r = curr_r + dr[i]
            new_c = curr_c + dc[i]
            # print("ㄴ new_r:", new_r, " new_c", new_c)
            
            if (0 <= new_r < n) and (0 <= new_c < m) and visited[new_r][new_c] == False:
                # print("- 지도 안에 있고, 방문한 적 없음")
                visited[new_r][new_c] = True
                # 원래 못 가는 땅
                if graph[new_r][new_c] == 0:
                    # print("-- 원래 못가는 땅, 0 처리")
                    result[new_r][new_c] = 0
                # 원래 갈 수 있는 땅
                elif graph[new_r][new_c] == 1:
                    # print("-- 갈 수 있는 땅")
                    result[new_r][new_c] = result[curr_r][curr_c] + 1
                    queue.append((new_r, new_c))
    
    return result


def solution():
    n, m = map(int, input().split())

    graph = []
    goal_r = -1
    goal_c = -1
    for i in range(n):
        line = list(map(int, input().split()))
        graph.append(line)

        if 2 in line:
            goal_r = i
            goal_c = line.index(2)

    # result = dijkstra(graph, goal_r, goal_c)
    result = bfs(graph, goal_r, goal_c)
    for i in range(n):
        print(*result[i])

if __name__ == "__main__":
    solution()