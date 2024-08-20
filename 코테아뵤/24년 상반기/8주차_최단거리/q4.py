# 백준 11657번. 타임머신

"""
- N 개의 도시가 있고, 한 도시에서 출발하여 다른 도시에 도착하는 버스 M 개가 있음
    → N 개 노드, M 개 간선
- 각 버스는 A, B, C 로 나타낼 수 있는데
    - A는 시작 도시 → 시작 노드
    - B는 도착 도시 → 도착 노드
    - C는 버스를 타고 이동하는데 걸리는 시간 → 간선 가중치
- 시간 C가 양수가 아닌 경우가 있음
    - C = 0인 경우는 순간 이동을 하는 경우
    - C < 0 인 경우는 타임머신으로 시간을 되돌아 가는 경우
    **→ 음수 가중치 존재, 벨만-포드 사용**
- 1번 도시에서 출발해서 나머지 도로로 가는 가장 빠른 시간을 구해야 함
- 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 -1 출력
    **→ 벨만 포드로 음수 순환 확인, 음수 순환 존재 시 -1 출력**
- 그렇지 않다면 N-1 개 줄에 걸쳐 각 줄에 1번 도시에서 출발하여 2번 도시, 3번 도시, N 번 도시 가는 최단 시간 출력
- 해당 도시로 가는 경로가 없다면 -1 출력
---
- N : 노드 개수
- M : 간선 개수
- A : 시작 노드
- B : 도착 노드
- C : 간선 가중치
---
- 1 ≤ N ≤ 500
- 1 ≤ M ≤ 6,000 
    **→ 벨만 포드 시간 복잡도 O(V*E) = O(500*6,000) = $O(3*10^6)$ < $10^{10}$**
- 1 ≤ A, B ≤ N
- -10,000 ≤ C ≤ 10,000
---
- 시간 제한 1초
- 메모리 제한 256 MB

1. 노드 개수 N, 간선 개수 M 입력 받기
2. 그래프 생성
    1. 인접 리스트로 구현
3. M개 간선 정보 그래프에 추가
4. 벨만 포드로 1번 도시에서 출발하여 모든 도시로 가는 최단 거리 연산
    1. 최단 거리 배열 초기화
    2. N-1 번 반복문 실행 `range(N-1)`
        1. 모든 간선 접근 `range(N)`
        2. 간선을 거쳐 다른 노드로 가는 비용 계산
        3. 최단 거리 갱신
    3. 음수 순환 확인
        1. 음수 순환 존재 시 -1 출력 후 종료
5. 벨만 포드 결과 순서대로 출력
    1. 출발한 1번 노드 제외, 그 이후 노드까지 최단 거리 출력
    2. 특정 노드에 도달할 수 없어서 거리가 inf인 경우 -1 출력
"""

from sys import stdin
input = stdin.readline

def bellman_ford(graph, start, N):
    distance = [float('inf')] * (N+1)
    distance[start] = 0

    # 최단 거리 연산
    for _ in range(N-1):
        for i in range(1, N+1):
            for v, weight in graph[i]:
                if distance[i] != float('inf') and distance[i] + weight < distance[v]:
                    distance[v] = distance[i] + weight
    
    # 음수 순환 확인
    for i in range(1, N+1):
        for v, weight in graph[i]:
            if distance[i] != float('inf') and distance[i] + weight < distance[v]:
                return -1
    
    return distance

def solution():
    N, M = map(int, input().split())

    graph = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        st, ed, w = map(int, input().split())
        graph[st].append((ed, w))

    result = bellman_ford(graph, 1, N)

    if result == -1:
        print(result)
    else:
        # 시작 노드 제외 출력
        for dist in result[2:]:
            if dist == float('inf'):
                print(-1)
            else:
                print(dist)

if __name__ == "__main__":
    solution()