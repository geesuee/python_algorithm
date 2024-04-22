# DFS - 깊이 우선 탐색
# 스택과 재귀로 구현 가능

# ---------------
# 스택으로 구현
# - 1 : 그래프가 배열 내 연결 노드를 원소로 가지고 있는 형태일 때
# - 2 : 그래프가 두 노드 간 연결 여부를 0, 1로 표현하는 형태일 때
# ---------------
from collections import deque

def dfs_stack1(graph, start):
    visited = [False] * len(graph)
    stack = deque([start])
    path = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            # 방문 후 경로에 추가, 방문 여부 변경
            path.append(v)
            visited[v] = True
            print(v, end=' ')
            # 연결된 노드를 스택에 역순으로 push
            for neighbor in reversed(graph[v]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return path

def dfs_stack2(graph, start):
    visited = set()
    stack = deque([start])
    path = []

    while stack:
        v = stack.pop()
        if v not in visited:
            # 방문 후 경로에 추가, 방문한 노드로 추가
            path.append(v)
            visited.add(v)
            print(v, end=' ')
            # 연결된 노드를 스택에 역순으로 push
            for i in reversed(range(len(graph[v]))):
                if graph[v][i] == 1 and i not in visited:
                    stack.append(i)
    return path

# ---------------
# 재귀로 구현
# - 1 : 그래프가 배열 내 연결 노드를 원소로 가지고 있는 형태일 때
# - 2 : 그래프가 두 노드 간 연결 여부를 0, 1로 표현하는 형태일 때
# ---------------
def dfs_recursion1(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs_recursion1(graph, i, visited)

def dfs_recursion2(graph, start, visited=set()):
    visited.add(start)
    print(start, end=' ')

    for i in range(len(graph[start])):
        if graph[start][i] == 1 and i not in visited:
            dfs_recursion2(graph, i, visited)


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

    # 스택 실행
    dfs_stack1(graph1, 1)
    print(dfs_stack1(graph1, 1))

    dfs_stack2(graph2, 1)
    print(dfs_stack2(graph2, 1))


    # 재귀 실행
    visited = [False] * (V+1)
    dfs_recursion1(graph1, 1, visited)

    dfs_recursion2(graph2, 1)        