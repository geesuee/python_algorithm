# 백준 1446번. 지름길

"""
- 매일 차를 타고 D킬로미터 길이의 고속도로를 지남
- 커브가 많은 고속도로
- 고속도로 내 지름길이 존재함
    - 지름길은 시작점, 종료점, 길이로 이루어짐
    - 길이 = 가중치
    **→ 가중치가 각각 다른 그래프 내에서 최단 거리 탐색 = 다익스트라!**
- 모든 지름길은 일방통행, 고속도로를 역주행할 수 없음
    → 단방향 그래프
    **→ 이동 시, 돌아올 수 없음을 고려해야 함**
- 세준이가 운전해야 하는 거리의 최솟값 출력
    → 최단 경로 탐색
---
<aside>
💡 **문제에서 명시되진 않았지만 파악할 수 있는 조건**
- 고속도로 내 지점별 이동 최단 거리를 구해야 하기 때문에 고속도로 길이 = 노드 개수
- 고속도로 내 길이 1 = 노드 하나
- 지름길을 이용하지 않았을 때, 노드 간 이동 가중치 = 거리 차
- 모든 길은 일방통행, 역주행 할 수 없기 때문에
    - 도착 지점이 고속도로 길이를 넘어가는 지름길은 사용 X
    - 이전에 방문한 노드를 뒤로 가서 방문하는 경우 X, 
    그래프에 이전 노드와 연결된 간선은 없기 때문에 방문 여부는 고려할 필요 X
</aside>
---
- N : 지름길의 개수
    - 간선의 개수
- D : 고속도로 길이
---
- 0 < N ≤ 12
- 0 < D ≤ 10,000
- 0 ≤ 시작 위치, 도착 위치, 지름길 길이 ≤ 10,000
---
- 시간 제한 2초 ($10^{10} * 2$)
- 메모리 제한 128 MB

1. 지름길 개수 N, 고속도로 길이 D 입력 값 받기
2. 고속도로 길이 D 내 숫자 하나 하나가 노드, 크기가 D+1인 그래프 생성
    1. 노드 개수가 1,000 개를 넘기 때문에 인접 리스트로 구현
    2. 노드 숫자 그대로 인덱스 접근하기 위해 D+1 크기로 생성
3. 노드 개수에 맞춰 크기가 D+1인 최소 거리 배열 생성
    1. 마찬가지로 노드 숫자 그대로 인덱스 접근하기 위해 D+1 크기로 생성
4. 노드 간 기본 거리는 1, 그래프 내 노드 간 거리 1로 초기화
5. 지름길이 있는 경우 노드 간 거리 갱신
    1. **지름길의 도착지가 고속도로의 거리보다 크다면 고려하지 않음**
    (후진이 불가능한 도로이기 때문에 넘어가면 안됨)
6. 다익스트라로 출발 지점인, 즉 출발 노드인 0에서부터 최단 거리 탐색
7. 결과 배열에서 고속도로 길이 D까지 가는 최단 거리 값 조회하여 출력
"""

from sys import stdin
input = stdin.readline
import heapq

def dijkstra(graph, start, distance):
    priority_queue = [(0, start)]
    distance[start] = 0

    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)

        if curr_distance > distance[curr_node]:
            continue

        for i in graph[curr_node]:
            node = i[0]
            weight = i[1]
            new_distance = curr_distance + weight
            if new_distance < distance[node]:
                distance[node] = new_distance
                heapq.heappush(priority_queue, (new_distance, node))

    return distance
    

def solution():
    N, D = map(int, input().split())

    graph = [[] for _ in range(D+1)]
    distance = [float('inf')] * (D+1)

    # 노드 간 기본 간선 가중치
    for i in range(D):
        # 연결된 노드와 이동 가중치
        graph[i].append((i+1, 1))

    # 지름길 간선 가중치
    for _ in range(N):
        # 지름길 시작점, 끝점, 가중치
        st, ed, weight = map(int, input().split())
        if ed > D:
            continue
        graph[st].append((ed, weight))
    
    # 다익스트라로 최단 거리 연산
    result = dijkstra(graph, 0, distance)
    print(result[D])


if __name__ == "__main__":
    solution()