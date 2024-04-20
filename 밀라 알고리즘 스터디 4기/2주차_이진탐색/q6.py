# 백준 1920번 수 찾기

"""
- N개의 정수가 주어짐
- 이 안에 X라는 정수가 존재하는 지 확인
---
- N : 주어지는 수의 개수
- A[1], A[2], … A[N] : 주어지는 N개 정수
- M : 탐색해야하는 수의 개수
---
- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- -2^31 ≤ 주어지는 수 ≤ 2^31

1. N 값 입력 받기
2. N 개 주어진 수 입력 받기
3. M 값 입력 받기
4. M 개 주어진 수 입력 받기
5. Counter 함수로 주어진 수 내 요소 카운트
6. Counter 내 값이 있는지 조회하여, 있으면 1 없으면 0 출력
---
주어진 값이 A 안에 있는지 이진 탐색을 통해 찾을 수도 있지만,
이진 탐색 풀이 시간 복잡도 O(NlogN), 위의 풀이 O(N)이라서 위 풀이 선택
"""

# Counter 함수 활용 풀이
from sys import stdin
input = stdin.readline
from collections import Counter

# def solution():
#     input()  # N 값, 받아도 쓸 곳 없어서 메모리 할당 X
#     A = list(map(int, input().split()))
#     input()  # M 값, "
#     X = list(map(int, input().split()))

#     counter = Counter(A)

#     for x in X:
#         if counter[x] == 0:
#             print(0)
#         else:
#             print(1)

# 이진 탐색 풀이
def binary(target, A, start, end):
    if start > end: # 찾는 수가 없으면
        return 0

    mid = (start + end) // 2

    if target == A[mid]:
        return 1
    elif target > A[mid]:
        return binary(target, A, mid+1, end)
    elif target < A[mid]:
        return binary(target, A, start, mid-1)

def solution():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    input()
    X = list(map(int, input().split()))

    for x in X:
        print(binary(x, A, 0, N-1))


if __name__ == "__main__":
    solution()