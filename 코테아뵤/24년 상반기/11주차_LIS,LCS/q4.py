# 백준 9252번. LCS2

"""
- 두 문자열의 LCS 길이와, LCS 문자열 출력
- 첫번째 줄에 길이를, 두번째 줄에 문자열을 출력
- LCS 가 여러 가지인 경우에는 아무거나 출력
- LCS 길이가 0인 경우에는 둘째 줄을 출력하지 않음
---
- 1 ≤ 문자열 길이 ≤ 1,000
---
- 시간 제한 2 초
- 메모리 제한 256 MB

1. 문자열 한 줄씩 입력 받기
2. DP 기반 LCS 함수 구현
    1. LCS 길이 연산
        1. 각 문자열 길이 + 1 크기의 이차원 배열 생성
        2. 이중 반복문으로 한 문자씩 접근
        3. 비교하는 문자가 같으면, 이전 값에서 + 1 으로 값 입력
        4. 다르면 문자 하나씩 이전 값 중 max 으로 값 입력
        5. 이차원 배열의 맨 끝 값이 LCS 길이
    2. **LCS 문자열 탐색 (이전 문제에 없던 부분!)**
        1. 이차원 배열의 맨 끝 값, 각 문자열의 길이에서부터 역순으로 접근
        2. 비교하는 문자열이 같으면 해당 문자를 LCS 문자열에 추가
        3. dp로 연산한 값이 어떤 것이 크냐에따라 특정 부분 -1 하면서 접근
        4. 마지막으로 구한 LCS 문자를 역순으로 접근했기 때문에 reverse
3. LCS 길이와 LCS 문자열 출력
"""

from sys import stdin
input = stdin.readline

def lcs(X, Y):
    x = len(X)
    y = len(Y)

    dp = [[0] * (y+1) for _ in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs_legth = dp[x][y]

    lcs_str = []
    i, j = x, y
    while i > 0 and j > 0:

        if X[i-1] == Y[j-1]:
            lcs_str.append(X[i-1])
            i -= 1
            j -= 1
        
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        
        elif dp[i-1][j] <= dp[i][j-1]:
            j -= 1
    
    lcs_str.reverse()

    return lcs_legth, ''.join(lcs_str)


def solution():
    X = input().strip()
    Y = input().strip()

    lcs_length, lcs_str = lcs(X, Y)
    print(lcs_length)
    print(lcs_str)

if __name__ == "__main__":
    solution()