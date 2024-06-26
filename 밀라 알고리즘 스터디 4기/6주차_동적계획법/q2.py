# 백준 9095번. 1,2,3 더하기

"""
- 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지
    - 1 + 3 과 3 + 1 은 별개의 케이스
    - 조합이 아닌 순열을 구해야 함
    - 경우의 수
        - 1+1+1+1
        - 1+1+2
        - 1+2+1
        - 2+1+1
        - 2+2
        - 1+3
        - 3+1
- 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수 연산
---
- T : 테스트 케이스 수
- n : 주어지는 정수, 1,2,3의 합으로 만들어야 하는 수
---
- 0 < n < 11

0. 점화식 찾기
    - f(1) = 1
        - 1
    - f(2) = 2
        - 1 + 1
        - 2
    - f(3) = 4
        - 1 + 1 + 1
        - 1 + 2
        - 2 + 1
        - 3
    - f(4) = 7
        - 1 + 1 + 1 + 1
        - 1 + 1 + 2
        - 1 + 2 + 1
        - 2 + 1 + 1
        - 3 + 1
        - 1 + 3
        - 2 + 2    

    f(6)을 구한다고 생각했을 때
    6 = 5 + 1 = 4 + 2 = 3 + 3
    1, 2, 3으로 6을 만들 수 있는 경우의 수는
    5를 만들 수 있는 경우의 수(=f(5))에 모두 + 1
    4를 만들 수 있는 경우의 수(=f(4))에 모두 + 2
    3을 만들 수 있는 경우의 수(=f(3))에 모두 + 3
    때문에 $f(n) = f(n-1) + f(n-2) + f(n-3)$
---
1. 테스트 케이스 수 입력 받기
2. 테스트 케이스 수 만큼 반복문 실행
3. 테스트 케이스별로 주어진 n에 대하여 동적 계획법 구현
    - $f(n) = f(n-1) + f(n-2) + f(n-3)$
        - 점화식 안에 n-3이 있기 떄문에 f(1), f(2), f(3) 값 미리 연산해 넣어줌
    - 태뷸레이션으로 상향식 연산
        - 값을 저장하는 tab 생성
        - n=1, n=2, n=3 일 때 값 연산하여 tab에 저장
        - 4 ≤ n < 11 구간 반복문으로 값 연산하여 tab에 저장
    - n번째 값 반환
"""

from sys import stdin
input = stdin.readline

def solution():
    T = int(input())
    
    dp_tab = {}
    dp_tab[1] = 1
    dp_tab[2] = 2
    dp_tab[3] = 4

    for i in range(4, 11):
        dp_tab[i] = dp_tab[i-1] + dp_tab[i-2] + dp_tab[i-3]

    for _ in range(T):
        n = int(input())
        print(dp_tab[n])

if __name__ == "__main__":
    solution()