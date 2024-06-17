# 백준 11659번. 구간 합 구하기 4

"""
- 수 N 개가 주어졌을 때, i 번째 수부터 j 번째 수까지 합을 구하는 프로그램
    → 구간 합 연산
---
- N : 수의 개수(=배열의 길이)
- M : 구간 합을 구해야 하는 횟수
- $n_i$ : 배열 원소 값
- i : 구간 합 연산 시, 구간 시작점
- j : 구간 합 연산 시, 구간 종료점
---
- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- 1 ≤  $n_i$  ≤ 1,000
- 1 ≤ i ≤ j ≤ N
→ 구간 길이는 j-i+1, 최악의 경우 N
단순히 하나씩 값에 접근하여 구간 합을 구하면 구간 합 연산 당 시간 복잡도 O(N),
이 문제에서는 구간 합 연산을 M 번씩 해야하기 때문에 총 시간 복잡도 O(N*M) = O($10^{10}$) 시간 초과 💥
→ **세그먼트 트리를 활용**하여 구간 합을 구하면 구간 합 연산 당 시간 복잡도 **O(logN)**,
이 문제에서 O(M*logN) = O($10^5*5$) < O($10^{10}$)

1. 배열 길이 N, 구간 합 연산 수 M 입력 받기
2. 배열 원소 값 입력 받기
3. M개 만큼 구간 합 연산하여 결과 출력
---
- 세그먼트 트리로 구간 합 구현
    - 세그먼트 트리 생성
        - 세그먼트 트리 크기는 N 보다 크거나 같은 2의 최소 거듭제곱 수 * 2
    - 세그먼트 트리 값 초기화
        - 재귀 방식으로 구간을 반씩 쪼개어 구간 합 구함
        - 왼쪽 자식 노드와 오른쪽 자식 노드를 합산하여 부모 노드 값 연산
    - 세그먼트 트리 탐색하여 구간 합 연산
        - 재귀 방식으로 구간 합 트리를 탐색하여, 구간에 해당하는 값만 찾아 합산
            - 케이스 1: 구간 합을 구해야 하는 구간이 현재 탐색 구간에 없음 ⇒ 0 반환
            - 케이스 2: 구간 합을 구해야 하는 구간이 현재 탐색 구간에 완전히 포함됨 ⇒ 현재 노드 값 반환
            - 케이스 3: 구간 합을 구해야 하는 구간이 현재 탐색 구간에 부분적으로 포함됨 ⇒ 구간을 반쪼개 탐색
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def init_segment_tree(arr):
    # 트리 생성
    N = len(arr)
    size = 2 * (2 ** (N-1).bit_length())
    tree = [0] * size

    # 재귀로 트리 값(=구간 합 값) 연산
    def build_segment_tree(arr, node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build_segment_tree(arr, 2*node, start, mid)
            build_segment_tree(arr, 2*node+1, mid+1, end)
            tree[node] = tree[2*node] + tree[2*node+1]
    
    build_segment_tree(arr=arr, node=1, start=0, end=N-1)

    return tree

def get_segment_sum(tree, L, R, N):
    # 재귀로 트리 탐색
    def find_segment_sum(L, R, node, start, end):
        # 1) 구간 안 겹침
        if R < start or L > end:
            return 0
        # 2) 구간 다 겹침
        if L <= start and end <= R:
            return tree[node]

        # 3) 구간 일부 겹침
        mid = (start + end) // 2
        left_sum = find_segment_sum(L, R, 2*node, start, mid)
        right_sum = find_segment_sum(L, R, 2*node+1, mid+1, end)
        return left_sum + right_sum
    
    return find_segment_sum(L, R, 1, 0, N-1)

def solution():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 세그먼트 트리 생성
    tree = init_segment_tree(arr)

    for _ in range(M):
        i, j = map(int, input().split())
        # 구간 합 연산
        # 자식 노드에 편하게(*2) 접근하기 위해 인덱스를 1부터 시작하게했음으로 -1씩 해서 접근
        print(get_segment_sum(tree, i-1, j-1, N))


if __name__ == "__main__":
    solution()