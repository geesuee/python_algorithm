# 백준 2805번 랜선 자르기

"""
- N개의 랜선을 만들어야 함
- 길이가 제각각인 K개의 랜선을 가지고 있음
- 이를 잘라서 같은 길이의 랜선을 만들고 싶음
- N개보다 많이 만드는 것도 N개를 만드는 것에 포함
- 최대 랜선 길이 구하기
---
- K : 이미 가지고 있는 랜선 개수, 1 ≤ K ≤ 10,000
- N : 필요한 랜선 개수, K를 잘라서 만들어야 하는 랜선 개수
---
- 찾아야 할 값 : 잘린 랜선의 최대 길이
- 조건 : 잘린 랜선의 개수가 N개 이상이어야 함


1. K, N 입력 값 받기
2. K개의 랜선 길이 입력 값 받기
3. 이진 탐색 구현
    1. 첫 start = 1, end = 가진 K개의 랜선 중 max
    2. 구간이 있을 때까지 계속 반복(start ≤ end)
    3. 잘린 랜선의 개수 연산
    4. 잘린 랜선의 개수가 목표치보다 적다면
        → 더 잘게 쪼개야 함, 구간을 더 적은 수로 잡아야 함
        → end = mid - 1
    5. 잘린 랜선의 개수가 목표치보다 크다면
        → 더 크게 잘라도 됨, 구간을 더 큰 수로 잡아야 함
        → start = mid + 1
"""

from sys import stdin
input = stdin.readline

def solution():
    K, N = map(int, input().split())
    k_list = [int(input()) for _ in range(K)]
    
    start, end = 1, max(k_list)

    while start <= end:
        line_count = 0
        mid = (start + end) // 2

        for k in k_list:
            line_count += k // mid
        
        if line_count >= N:
            start = mid + 1
        else:
            end = mid - 1
    
    print(end)

if __name__ == "__main__":
    solution()