# 백준 11053번. 가장 긴 증가하는 부분 수열

"""
- 수열 A 가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구해야 함
    **→ 가장 긴 증가하는 부분 수열 = LIS** 
---
- N : 수열 A 의 크기
- $A_i$ : 수열 A 의 원소
---
- 1 ≤ N ≤ 1,000
- 1 ≤ $A_i$ ≤ 1,000
---
- 시간 제한 1 초
- 메모리 제한 256 MB

1. 수열 A 의 크기 N 입력 받기
2. 수열 A 원소 N 개 입력 받기
3. LIS 함수 생성
    1. 이분 탐색 기반 LIS 알고리즘 구현
    2. bisect 라이브러리 사용
4. 수열 A 에 대한 LIS 탐색하여 출력
"""

from sys import stdin
input = stdin.readline
import bisect

def lis(arr):
    lis = []

    for num in arr:
        pos = bisect.bisect_left(lis, num)

        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    
    return len(lis)

def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    print(lis(arr))

if __name__ == "__main__":
    solution()