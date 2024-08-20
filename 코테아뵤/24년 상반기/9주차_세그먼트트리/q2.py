# 백준 2042번. 구간 합 구하기

"""
- 어떤 N 개의 수가 주어짐
- 중간 수의 변경이 빈번히 일어나고, 그 중간에 어떤 구간의 합을 구해야 함
    → 값 수정이 있는 구간 합 구하기
---
- N : 수의 개수(=배열의 길이)
- M : 수의 변경이 일어나는 횟수
- K : 구간의 합을 구하는 횟수
- a
    - 1이면, b 번째 수를 c 로 바꾸고
    - 2이면, b 부터 c 까지 구간 합 연산
---
- 1 ≤ N ≤ 1,000,000
- 1 ≤ M ≤ 10,000
- 1 ≤ K ≤ 10,000
→ 구간 길이는 최악의 경우 N
단순히 하나씩 값에 접근하여 구간 합 연산 시 시간 복잡도 O(N),
이 문제에서는 구간 합 연산을 K 번씩 해야하기 떄문에 총 시간 복잡도 O(N*K)
= O($10^{10}$) 시간 초과 💥
→ **세그먼트 트리를 활용**하여 구간 합 연산 시
- 세그먼트 트리 생성 시간 복잡도 O(N)
- M 번 세그먼트 트리 수정 시간 복잡도 O(M*logN)
- K 번 구간 합 연산 시간 복잡도 O(K*logN)
= 총 $O(N + M*logN + K*logN) ≈ O((M+K)logN)$
이 문제에서 약 $O(20,000*6) = O(12*10^4) < O(10^{10})$

1. 배열 길이 N, 값 수정 횟수 M, 구간 합 연산 횟수 K 입력 받기
2. 배열 원소 값 N 개 입력 받기
3. 세그먼트 트리 만들어 값 초기화 하기
4. M+K 회만큼 값 수정 혹은 구간 합 연산 관련 수 입력 받기
    1. a 값이 1이면, 세그먼트 트리 값 수정
    2. a 값이 2이면, 세그먼트 트리 탐색하여 구간 합 연산하여 출력
---
- 세그먼트 트리로 구간 합 구현
    - 세그먼트 트리 생성
        - 세그먼트 트리 크기는 편의상 4N 으로 지정
    - 세그먼트 트리 값 초기화
        - 리프 노드 값 추기화
        - 자식 노드 값의 합으로 부모 노드 연산
    - 세그먼트 트리 내 값 수정
        - 특정 원소 값을 갖는 리프 노드 찾아서 수정
        - 해당 노드가 영향을 주는 부모 노드 찾아서 수정
    - 세그먼트 트리 탐색하여 구간 합 연산
"""

import sys
input = sys.stdin.readline

def init_segment_tree(arr):
    N = len(arr)
    tree = [0] * (4*N)

    for i in range(N):
        tree[N+i] = arr[i]
    for i in range(N-1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]
    
    return tree

def update_segment_tree(tree, idx, value, N):
    idx += N
    tree[idx] = value

    while idx > 1:
        idx //= 2
        tree[idx] = tree[2*idx] + tree[2*idx+1]
    
    return tree

def query(tree, left, right, N):
    left += N
    right += N
    sum = 0

    while left < right:
        if left % 2 == 1:
            sum += tree[left]
            left += 1
        if right % 2 == 1:
            right -= 1
            sum += tree[right]
        left //= 2
        right //= 2

    return sum

def solution():
    N, M, K = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(int(input()))

    tree = init_segment_tree(arr)

    for _ in range(M+K):
        a, b, c = map(int, input().split())
        b -= 1
        if a == 1:
            tree = update_segment_tree(tree, b, c, N)
        else:
            print(query(tree, b, c, N))

if __name__ == "__main__":
    solution()