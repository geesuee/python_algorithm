# 백준 9251번. LCS

"""
- 두 문자열의 LCS 를 찾아서 LCS 의 길이 출력
- 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1,000글자
    **→ DP 기반 LCS 알고리즘 구현**
---
- 1 ≤ 문자열 길이 ≤ 1,000 
    **→ DP 기반 LCS 알고리즘 시간 복잡도 $O(N^2)$**
    **→ 이 문제에서 최대 $O(10^6)$**
---
- 시간 제한 Python3 은 2 초
- 메모리 제한 256 MB

1. 문자열 한 줄씩 입력 받기
2. DP 기반 LCS 함수 구현
    1. 문자열 길이 + 1 크기 2차원 배열 생성
    2. 이중 반복문으로 한 글자씩 접근
    3. 0행, 0열 값은 0으로 초기화
    4. 비교하는 두 문자가 같은 경우, +1
    5. 두 문자가 다른 경우, max 연산
3. LCS 길이 출력
"""

from sys import stdin
input = stdin.readline

def lcs(X, Y):
    x = len(X)
    y = len(Y)

    L = [[0] * (y+1) for _ in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):

            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[x][y]

def solution():
    X = input().strip()
    Y = input().strip()

    print(lcs(X, Y))


if __name__ == "__main__":
    solution()