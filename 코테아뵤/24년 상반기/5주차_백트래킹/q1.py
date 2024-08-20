# 백준 15651번. N과 M (9)

"""
- N개의 자연수와 자연수 M이 주어졌을 때
- N개의 자연수 중에서 M개를 고른 수열
- M개 수열을 오름차순으로 출력, 중복은 출력하지 않음
---
- N : 수열을 만들어야 하는 자연수 개수
- M : 수열의 길이
---
- 1 ≤ M ≤ N ≤ 8

solution1 : permutations 라이브러리 활용 풀이
    1. N, M 입력 값 받기
    2. N 개 만큼 주어지는 자연수 입력 받아 리스트로 변환
    3. permutations 로 순열 연산
    4. 연산 결과 중복 제거
    5. 연산 결과 오름차순 정렬
    6. 출력

solution2 : 백트래킹 풀이
    1. N, M 입력 값 받기
    2. N 개 만큼 주어지는 자연수 입력 받아 리스트로 변환
    3. 백트래킹 구현
        1. 순열 완성 조건 명시 → 완성 시 값 반환 혹은 출력
        2. 주어진 자연수를 하나씩 돌면서 방문한 적 있는 지 확인
            - 없다면 만들고 있는 순열에 추가하고 방문 처리
            - 백트래킹 함수 재귀 실행
            - 끝까지 돌고 왔다면 가지치기로 이전 값 복원
                - 만들고 있는 순열에서 다시 pop
                - 미방문 처리
    4. 연산 결과 중복 제거
    5. 연산 결과 오름차순 정렬
    6. 출력
"""

from sys import stdin
input = stdin.readline
from itertools import permutations

# permutations 라이브러리 활용 풀이
def solution1():
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    p = permutations(numbers, M)
    p = sorted(set(p))

    for i in p:
        print(*i, sep=' ')


# 백트래킹 풀이
def backtracking(N, M, numbers, visitied, answer):
    # 길이가 M이 되면 반환
    if len(answer) == M:
        return[answer[:]]

    # 주어진 자연수를 돌면서 선택
    result = []
    for i in range(N):
        if visitied[i] == 0:
            answer.append(numbers[i])
            visitied[i] = 1
            result.extend(backtracking(N, M, numbers, visitied, answer))
            answer.pop()
            visitied[i] = 0
    return result


def solution2():
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 선택한 수인지 확인
    # - 한 숫자가 여러 번 들어갈 수 있기 때문에 not in으로 확인하지 않고 visited 사용
    visited = [0] * N
    answer = []
    
    result = backtracking(N, M, numbers, visited, answer)
    sorted_unique_result = sorted(set(map(tuple, result)))

    for r in sorted_unique_result:
        print(*r, sep=' ')

if __name__ == "__main__":
    solution1()
    solution2()