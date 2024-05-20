# 백준 2579번. 계단 오르기

"""
- 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임
- 각각의 계단에는 일정한 점수가 쓰여있음
- 계단을 밟으면 계단에 쓰여있는 점수를 얻게 됨
- 계단은 **한 번에 한 계단씩 또는 두 계단씩** 오를 수 있음
- **연속된 세 개의 계단을 모두 밟아서는 안됨** (시작점은 계단에 포함되지 않음)
- 얻을 수 있는 총 점수의 최댓값 연산
---
- $N$ : 계단의 개수
- $X_i$ : 각 계단의 점수
---
- 1 ≤ $N$ ≤ 300
- 1 ≤ $X_i$ ≤ 10,000

1. 계단 수 입력 값 받기
2. 각 계단의 점수 입력 값 받기
3. 동적 계획법 구현
    - $f(n) = max(f(n-3)+stairs[n-1], f(n-2)) + step[n]$
        - 세 개 계단을 연속으로 밟을 수 없기 때문에
        - n번째 계단까지 최대 점수는 아래 둘 중 큰 값
            1) n-3, n-1 계단 밟은 점수
            2) n-2 계단 밟은 점수
        - **점화식 안에 n-3이 있기 때문에 f(0), f(1), f(2) 값을 미리 연산해 넣어줌(음수로 재귀 돌지 않도록)**
    - 메모이제이션으로 하향식 연산
        - 값을 저장하는 memo 값이 None이면 생성
        - n=0,1,2 일 때 값 미리 연산
        - 값을 저장하는 memo 값 안에 찾는 n번째 값이 저장되어 있으면 반환
        - 점화식을 재귀로 구현하여 n번째 값 연산하는 코드 작성
        - n번째 값 반환
"""

from sys import stdin
input = stdin.readline

def solution():
    N = int(input())

    stairs = [0] * (N+1)
    for i in range(1, N+1):
        stairs[i] = int(input())

    def dp_memo(n, memo=None):
        if memo is None:
            memo = {}

        if n <= 1:
            return stairs[n]
        
        if n >= 2:
            memo[2] = stairs[1] + stairs[2]

        if n in memo:
            return memo[n]    
        
        memo[n] = max(dp_memo(n-2, memo), dp_memo(n-3, memo)+stairs[n-1]) + stairs[n]
        return memo[n]

    print(dp_memo(N))

if __name__ == "__main__":
    solution()