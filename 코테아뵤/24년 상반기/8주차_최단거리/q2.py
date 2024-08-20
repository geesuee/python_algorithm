# 백준 11403번. 경로 찾기

"""
- 가중치 없는 방향 그래프 G
- 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 탐색
- 인접 행렬을 입력 받아 특정 정점 i에서 j로 가는 경로가 있는지 없는지 출력
    **→ 모든 정점을 대상으로, 특정 정점에서 다른 특정 정점까지 거리 연산 = 플로이드 와샬**
---
- N : 정점의 개수
- graph : 그래프는 인접 행렬 형태로 입력
---
- 1 ≤ N ≤ 100 
    → 플로이드 와샬 시간 복잡도 $O(N^3)$, 이 경우 최대 $10^6$, $10^{10}$(=1초) 안쪽이라 사용 가능
---
- 시간 제한 1초
- 메모리 제한 256 MB

1. 노드 개수 N 입력 받기
2. 그래프 인접 행렬 입력 받기
3. 플로이드 와샬로 모든 노드 간 연결 여부 확인
    1. 간선 가중치가 다를 때에는 플로이드 와샬로 모든 노드 간 최단 거리 연산 가능
    2. 간선 가중치가 동일하고, 연결 여부만 확인할 때는 삼중 반복문으로 거리 업데이트 하는 코드 단순화 가능
    ---
    - 최단 거리 연산이 아니기 때문에, 연결 여부 저장하고 반환하는 배열 초기 값은 0
    - 인접 행렬 값 확인하여 노드 간 연결 여부 초기화(조건 상 i 노드에서 i 노드는 연결되지 않은 것으로 봄)
    - 삼중 반복문으로 가운데 노드를 끼워 노드 간 연결 관계 갱신
4. 플로이드 와샬 결과 출력
"""

from sys import stdin
input = stdin.readline

def floyd_warshall(N, graph):
    connected = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                connected[i][j] = 0
            elif graph[i][j] != 0:
                connected[i][j] = 1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if connected[i][j] == 0:
                    connected[i][j] = connected[i][k] and connected[k][j]

    return connected

def solution():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    connected = floyd_warshall(N, graph)

    for c in connected:
        print(*c, end="\n")

if __name__ == "__main__":
    solution()