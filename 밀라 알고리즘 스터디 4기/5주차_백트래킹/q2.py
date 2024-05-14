# 백준 15651번. N과 M (3)

"""
- 자연수 N과 M이 주여졌을 때, 1부터 N까지 자연수 중에서 M개 고른 순열
- 같은 수를 여러 번 골라도 됨
    → 중복 순열
- 중복 없이, 오름차순으로 출력
---
- N : 1~N 까지 자연수가 주어짐, 선택할 수 있는 자연수 범위
- M : 고를 수의 개수
---
- 1 ≤ M ≤ N ≤ 7

solution1 : product 라이브러리 활용 풀이
    1. N, M 입력 값 받기
    2. 1~N 선택할 수 있는 수 리스트 생성
    3. 중복 순열 연산
        1. product 로 중복 순열 연산
    4. 연산 결과 중복 제거
    5. 연산 결과 오름차순 정렬
    6. 출력

solution2 : 백트래킹 풀이
    1. N, M 입력 값 받기
    2. 1~N 선택할 수 있는 수 리스트 생성
    3. 중복 순열 연산
        1. 백트래킹 풀이
            1. 순열 완성 조건 명시(=길이가 M) → 완성 시 값 반환
            2. 주어진 자연수를 하나씩 돌면서 순열에 추가(중복 가능하니 중복 체크 X)
            3. 백트래킹 함수 재귀 실행
            4. 재귀가 끝까지 돌고 왔다면 가지치기로 이전 값 복원
                - 만들고 있는 순열에서 다시 pop
    4. 연산 결과 중복 제거
    5. 연산 결과 오름차순 정렬
    6. 출력
"""

from sys import stdin
input = stdin.readline
from itertools import product

# product 라이브러리 활용 풀이
def solution1():
    N, M = map(int, input().split())
    numbers = list(range(1, N+1))
    
    p = product(numbers, repeat=M)
    p = sorted(set(p))

    for i in p:
        print(*i, sep=" ")

# 백트래킹 풀이
def backtracking(N, M, numbers, answer):
    if len(answer) == M:
        return [answer[:]]

    result = []
    for n in numbers:
        answer.append(n)
        result.extend(backtracking(N, M, numbers, answer))
        answer.pop()
    return result

def solution2():
    N, M = map(int, input().split())
    numbers = list(range(1, N+1))

    answer = []
    result = backtracking(N, M, numbers, answer)
    sorted_unique_result = sorted(set(map(tuple, result)))

    for r in sorted_unique_result:
        print(*r, sep=" ")


if __name__ == "__main__":
    # solution1()
    solution2()