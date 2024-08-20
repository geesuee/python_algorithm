# 백준 2644번. 촌수 계산

"""
- 부모와 자식 사이는 1촌, 이로부터 사람들 간의 촌수 계산
    **→ 부모-자식 양방향 연결, 양방향 그래프**
    **→ 부모 노드, 자식 노드 간 간선 가중치 1**
    **→ 모든 간선 가중치가 1이고, 특정 노드로 부터 모든 노드로 가는 최단 거리가 아니라 특정 노드 둘 간의 최단 거리를 찾으면 되기 때문에 BFS 로 구현**
- 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램 작성
    **→ 부모-자식 간선 가중치 1로부터 출발, 노드 간 가중치 합산하여 촌수 계산**
- 사람들은 1~n 의 연속된 번호로 표시됨
    **→ 노드 1~n**
- 촌수를 구해야 하는 두 사람의 친척 관계가 없어 촌수를 계산할 수 없으면 -1 출력
---
- n : 노드 개수, 1~n 노드
- a, b : 촌수를 계산해야 하는 서로 다른 두 사람의 번호
- m : 부모 자식 간 관계 개수, 간선 개수
- x, y : x가 부모, y가 자식
---
- 1 ≤ n ≤ 100 
    **→ 노드가 100개 이하이니, 인접 행렬로 구현**

1. 노드 개수 n 입력 받기
2. 서로 간 촌수를 구해야 하는 a, b 입력 받기
3. 부모-자식 관계(=간선 연결 관계) 수 m 입력 받기
4. 인접 행렬 그래프 생성
5. m 만큼 반복문 실행하여 양방향 연결 관계 그래프에 추가
6. BFS로 a 노드로부터 b 노드까지 최단 거리 경로 연산
    1. 큐 생성, 출발 노드 넣어 초기화
    2. 노드별 방문 여부 확인할 배열 생성, 출발 노드 방문 처리
    3. **경로 연산을 위해 부모 노드가 무엇인지 저장할 배열 생성**
    4. 큐에 값이 있는 한 반복문 수행
        1. 큐에서 맨 앞에 있는 값 추출
        2. **해당 값이 도착 노드이면 경로 연산하여 return**
            - 도착 노드에서부터 부모 노드를 거꾸로 타고 올라가서 경로 연산
        3. 아니면, 해당 노드 연결 관계 접근하여
        연결된 노드이면서 방문하지 않은 노드 탐색
            - 위 노드에 차례로 방문하여 방문 처리, 부모 노드 저장, 큐에 추가
        4. 큐에 있는 모든 값을 돌 때까지 도착 노드를 방문하지 않았으면, 이는 연결될 수 없는 관계, 경로 값 None 리턴
7. 반환 경로가 없으면 -1 출력, 경로가 있으면 경로 길이에서 -1 해서 출력
    1. 경로에 출발 노드도 들어간 상태, 출발 노드에서 도착 노드까지 거리만 계산하려면 경로 길이 - 1
"""

from sys import stdin
input = stdin.readline
from collections import deque

def bfs(graph, start, end):
    n = len(graph) - 1
    queue = deque([start])
    visited = [False] * (n+1)
    parent = [None] * (n+1)
    visited[start] = True

    while queue:
        v = queue.popleft()
        if v == end:
            # 목표에 도달하면 경로 생성
            path = []
            while v is not None:
                path.append(v) # 현재 노드 경로에 추가 
                v = parent[v]  # 부모 노드로 타고 올라감(=이전 경로)
            # path.reverse() # 도착 노드에서부터 타고 올라왔으니 뒤집음
            return path

        for i in range(1, n+1):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                parent[i] = v
                queue.append(i)

    return None  # 목표 노드에 도달 할 수 없는 경우

def solution():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())

    graph = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        p, c = map(int, input().split())
        graph[p][c] = 1
        graph[c][p] = 1

    path = bfs(graph, a, b)

    if path is None:
        print(-1)
    else:
        print(len(path)-1) # 경로에 시작 노드가 들어가 있기 때문에 -1

if __name__ == "__main__":
    solution()