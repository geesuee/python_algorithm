# 백준 2491번. 수열

"""
- 0 에서부터 9 까지의 숫자로 이루어진 N 개의 숫자가 나열된 수열
- 그 수열 안에서 
**연속해서** 커지거나(같은 것 포함) **연속해서** 작아지는(같은 것 포함) 
수열 중 가장 길이가 긴 것을 찾아내어 그 길이 출력
    **→ LIS 알고리즘 사용
    (LIS 알고리즘은 연속 여부를 따지지 않지만, 이 문제에서는 따져줘야함)**
    **→ 원본 수열로 LIS 실행, 역순 배열 후 LIS 실행 후 두 값 비교하여 긴 값 출력**
---
- N : 수열의 길이
---
- 1 ≤ N ≤ 100,000
---
- 시간 제한 1 초
- 메모리 제한 128 MB

1. N 값 입력 받기
2. N 개의 수열 내부 값 입력 받기
3. DP 기반 LIS 탐색 함수 생성
4. 원본 수열로 LIS 탐색
5. 역순 수열로 LIS 탐색
6. 둘 중 더 큰 값 출력
"""

from sys import stdin
input = stdin.readline

def lis(arr):
    if not arr:
        return 0

    # DP 배열을 arr와 동일한 크기로 초기화하고 각 위치의 초기값을 1로 설정
    dp = [1] * len(arr)
    
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            dp[i] = dp[i - 1] + 1

    # dp 배열에서 최댓값이 최장 증가 연속 부분 수열의 길이
    return max(dp)

def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    arr_rev = list(reversed(arr))

    lis1 = lis(arr)
    lis2 = lis(arr_rev)

    print(max(lis1, lis2))

if __name__ == "__main__":
    solution()