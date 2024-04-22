# BFS - 너비 우선 탐색
# 큐로 구현

# ---------------
# 큐로 구현
# - 1 : 그래프가 배열 내 연결 노드를 원소로 가지고 있는 형태일 때
# - 2 : 그래프가 두 노드 간 연결 여부를 0, 1로 표현하는 형태일 때
# ---------------
from collections import deque

def bfs_queue1(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        v = queue.popleft()
        if v not in visited:
            # 방문 후 경로에 추가, 방문한 노드로 추가
            path.append(v)
            visited.add(v)
            print(v, end=' ')
            # 연결된 노드를 큐에 삽입
            for neighbor in graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return path

def bfs_queue2(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        v = queue.popleft()
        if v not in visited:
            # 방문 후 경로에 추가, 방문한 노드로 추가
            path.append(v)
            visited.add(v)
            print(v, end=' ')
            # 연결된 노드를 큐에 삽입
            for i in range(len(graph[v])):
                if graph[v][i] == 1 and i not in visited:
                    queue.append(i)
    return path

# ---------------
# V : 노드의 개수
# E : 간선 개수
# edge : 노드 연결 관계
# 
# graph1 : 그래프가 배열 내 연결 노드를 원소로 가지고 있는 형태
# graph2 : 그래프가 두 노드 간 연결 여부를 0, 1로 표현하는 형태
# ---------------
if __name__ == "__main__":
    V = 7
    E = 6
    edge = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 7), (5, 6)]

    # graph1
    graph1 = [[] for _ in range(V+1)]
    for e in edge:
        st, ed = e
        graph1[st].append(ed)
        graph1[ed].append(st)
    # print(graph1)

    # graph2
    graph2 = [[0]*(V+1) for _ in range(V+1)]
    for e in edge:
        st, ed = e
        graph2[st][ed] = 1
        graph2[ed][st] = 1
    # print(graph2)

    # 큐 실행
    bfs_queue1(graph1, 1)
    print(bfs_queue1(graph1, 1))

    bfs_queue2(graph2, 1)
    print(bfs_queue2(graph2, 1))