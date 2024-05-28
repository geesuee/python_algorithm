# 프로그래머스. 배달

"""
- N개의 마을로 이루어진 나라, 각 마을에는 1부터 N까지 번호가 부여됨
    **→ 노드 1~N**
- 각 마을은 양방향으로 통행할 수 있는 도로로 연결됨
    **→ 양방향 그래프**
- 도로를 지날 때 걸리는 시간은 도로별로 다름
    **→ 가중치가 각각 다른 간선**
- 1번 마을에서 K 시간 이하로 이동할 수 있는 마을 개수 출력
---
- N : 마을 개수, 1~N 노드
- road : 마을 연결 도로 정보, 간선 정보
- K : 마을 간 최단거리 이동 시간 limit 기준, K 시간 이하 이동 가능 마을 탐색
---
- 1 ≤ N ≤ 50 → 노드 개수
- 1 ≤ len(road) ≤ 2,000 → 간선 개수
- 1 ≤ K ≤ 500,000

1. 그래프 생성
    1. 딕셔너리 형태의 인접 리스트에 연결 노드와 가중치 적재
2. 다익스트라로 1번 노드에서 모든 노드까지 이동 시간 확인
    1. 힙큐로 구현
    2. 힙큐에 (가중치, 노드) 정보 적재
    3. 방문 여부 확인할 집합 생성
    4. 모든 노드 이동 가중치를 무한 값으로 `float(’inf’)` 초기화
    5. 시작 노드 거리만 0으로 갱신
    6. 우선순위 큐를 돌면서, 거리가 가장 짧은 노드 정보 pop
    7. 방문 여부 확인, 방문하지 않았다면
        1. 방문 처리
        2. 해당 노드의 이웃한 노드까지 거리 업데이트
            - 반복문으로 해당 노드에 연결된 노드에 접근
            - 거리 연산, 최소 값 갱신
            - 다음 인접 거리를 계산 하기 위해 힙큐에 삽입
3. 이동 시간이 K 시간 이하인 마을 개수 출력
"""

import heapq

def dijkstra(graph, start):
    q = [(0, start)]
    visited = set()
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while q:
        curr_distance, curr_node = heapq.heappop(q)

        # 방문 확인
        if curr_node in visited:
            continue

        # 방문 처리
        visited.add(curr_node)

        # 이웃한 노드 거리 갱신
        for neighbor, weight in graph[curr_node].items():
            new_distance = curr_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(q, (new_distance, neighbor))
    
    return distances


def solution(N, road, K):
    graph = {i+1: {} for i in range(N)}
    
    for r in road:
        a, b, c = r
        if b in graph[a]:
            old = graph[a][b]
            new = c
            graph[a][b] = min(old, new)
        else:
            graph[a][b] = c
        
        if a in graph[b]:
            old = graph[b][a]
            new = c
            graph[b][a] = min(old, new)
        else:
            graph[b][a] = c

    # 그래프 확인
    # print("--- 그래프 ---")
    # for k, v in graph.items():
    #     print(k, v)
    # print("---------------")

    distances = dijkstra(graph, 1)

    for k, v in distances.items():
        print(k, v)

    count = 0
    for node, dist in distances.items():
        if dist <= K:
            count += 1

    return count

if __name__ == "__main__":
    # 테스트 케이스 1
    # N = 5
    # road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    # K = 3
    
    # 테스트 케이스 2
    N = 6
    road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    K = 4

    answer = solution(N, road, K)
    print()
    print("****")
    print(answer)
    print("****")