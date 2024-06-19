# 백준 11505번. 구간 곱 구하기

"""
- N 개의 수가 주어짐
- 중간에 수의 변경이 일어남
- 구간 곱을 구해야 함
- 구간 곱 값을 1,000,000,007로 나눈 나머지를 출력
---
- N : 수의 개수(=배열 길이)
- M : 수의 변경이 일어나는 횟수
- K : 구간의 곱을 구하는 횟수
- a : 연산 구분 숫자
    - 1인 경우, b번째 수를 c로 바꿈
    - 2인 경우, b부터 c까지 곱을 구하여 출력
---
- 1 ≤ N ≤ $10^6$
- 1 ≤ M ≤ $10^4$
- 1 ≤ K ≤ $10^4$
---
- 시간 제한 1 초
- 메모리 제한 256 MB

1. N, M, K 입력 받기
2. N 개 배열 원소 입력 받기
3. 세그먼트 트리 생성
4. M+K 횟수만큼 연산 진행
    - a 값이 1이면, 숫자 변경
    - a 값이 2이면, 구간 곱 연산하여 출력
    - 원소 위치를 나타내는 b 를 인덱스 번호로 변환하기 위해 -1
---
- 세그먼트 트리 활용
    - 세그먼트 트리 생성
        - 세그먼트 트리 크기는 편의상 4N
        - **구간 합 연산에서는 초기 값을 0으로 했지만, 곱에서는 1로 설정**
    - 세그먼트 트리 값 초기화
        - 리프 노드 값 초기화
        - 자식 노드 값의 곱으로 부모 노드 연산
    - 세그먼트 트리 내 값 수정
        - 특정 원소 값을 단독으로 갖는 리프 노드 찾아서 수정
        - 해당 노드가 영향을 주는 부모 노드 타고 올라가서 수정
    - 세그먼트 트리 탐색하여 구간 곱 연산
        - 구간을 반씩 쪼개어 탐색
"""

import sys
input = sys.stdin.read
write = sys.stdout.write

MOD = 1000000007

def build_tree(arr, tree, N):
    # 리프 노드에 값 채우기
    for i in range(N):
        tree[N + i] = arr[i]
    
    # 내부 노드 채우기
    for i in range(N - 1, 0, -1):
        tree[i] = (tree[2 * i] * tree[2 * i + 1]) % MOD
    
def update_tree(tree, idx, value, N):
    idx += N
    tree[idx] = value
    
    while idx > 1:
        idx //= 2
        tree[idx] = (tree[2 * idx] * tree[2 * idx + 1]) % MOD

def query(tree, left, right, N):
    result = 1
    left += N
    right += N

    while left < right:
        if left % 2:
            result = (result * tree[left]) % MOD
            left += 1
        if right % 2:
            right -= 1
            result = (result * tree[right]) % MOD
        left //= 2
        right //= 2
    
    return result

def solution():
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    M = int(data[idx + 1])
    K = int(data[idx + 2])
    idx += 3
    
    arr = [0] * N
    for i in range(N):
        arr[i] = int(data[idx])
        idx += 1
    
    # 세그먼트 트리 초기화
    tree = [1] * (2 * N)
    build_tree(arr, tree, N)
    
    results = []
    for _ in range(M + K):
        a = int(data[idx])
        b = int(data[idx + 1]) - 1
        c = int(data[idx + 2])
        idx += 3
        
        if a == 1:
            update_tree(tree, b, c, N)
        elif a == 2:
            results.append(query(tree, b, c, N))
    
    write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    solution()
