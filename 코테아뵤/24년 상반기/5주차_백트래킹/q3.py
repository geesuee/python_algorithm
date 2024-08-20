# 백준 1182번. 부분수열의 합

"""
- N개의 정수로 이루어진 수열
- 부분 수열 중, 그 수열 원소를 다 더한 값이 S가 되는 경우의 수
---
- N : 수열 내 정수의 개수
- S : 부분 수열 합이 되어야 할 수
---
- 1 ≤ N ≤ 20
- |S| ≤ 1,000,000
---
- 입출력 예시
    - N = 5, S = 0
    - 수열 = -7 -3 -2 5 8
    - 수열에 있는 수로 조합을 해서 합이 0이 되는 경우
    - (-3) + (-2) + 5 = 0
    - 경우의 수 1개 존재

1. N, S 입력 값 받기
2. 길이가 N인 수열 입력 값 받기
3. 백트래킹으로 합이 S가 되는 부분 수열 조합 찾기
    1. 종료 조건 명시 : 길이가 1 이상이고, 원소 합이 S
        → 종료 조건 충족 시, 부분 집합 개수 + 1
    2. 원 수열 내 값 하나씩 돌면서 부분 수열에 추가
    3. 백트래킹 재귀 실행
    4. 재귀가 끝까지 돌고나면 가지치기로 이전 상태 복원
        1. 부분 수열에서 pop
        2. 미방문 처리
"""

from sys import stdin
input = stdin.readline

def solution():
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))

    def backtracking(start, count, subset):
        if len(subset) > 0 and sum(subset) == S:
            count += 1

        for i in range(start, N):
            subset.append(numbers[i])
            count = backtracking(i+1, count, subset)
            subset.pop()
        return count

    count = backtracking(0, 0, [])
    print(count)

if __name__ == "__main__":
    solution()