# 백준 1759번. 암호 만들기

"""
- 암호는 서로 다른 L개의 알파벳 소문자들로 구성
- 최소 한 개의 모음(a, e, i, o, u) 포함
- 최소 두 개의 자음 포함
- 알파벳 사전순 배열
- 주어진 C개의 알파벳 중 L개를 사용하여 만들 수 있는 암호를 사전순으로 출력
---
- L : 암호의 길이
- C : 주어진 알파벳의 개수
---
- 3 ≤ L ≤ C ≤ 15

1. L, C 입력값 받기
2. C개 알파벳 입력 받기
3. 백트래킹으로 길이가 L이 되는 조합 찾기
    1. 종료 조건
        - 암호 길이가 L
        - 모음 1개 이상 포함
        - 모음 외 2개 이상 포함
    2. 주어진 알파벳 하나씩 접근하는 반복문 실행
        1. 방문한 적이 없는 알파벳이면, 암호에 추가, 방문 처리
        2. 재귀 실행
        3. 가지치기로 암호에서 빼고, 미방문 처리
4. 암호 사전 순 정렬, 중복 제거하여 출력
"""

from sys import stdin
inpurt = stdin.readline
from itertools import combinations

# 백트래킹 풀이
def solution1():
    L, C = map(int, input().split())
    alphabet = sorted(input().split())
    vowel = {'a', 'e', 'i', 'o', 'u'}

    def backtracking(start, answer, vowel_count, consonant_count):
        if len(answer) == L:
            if vowel_count >= 1 and consonant_count >= 2:
                print(''.join(answer))
                return

        for i in range(start, C):
            char = alphabet[i]
            answer.append(char)
            if char in vowel:
                backtracking(i+1, answer, vowel_count+1, consonant_count)
            else:
                backtracking(i+1, answer, vowel_count, consonant_count+1)
            answer.pop()

    backtracking(0,[],0,0)

# combinations 라이브러리 활용 풀이
def solution2():
    L, C = map(int, input().split())
    alphabet = sorted(input().split())
    vowel = set('aeiou')

    def is_valid(password):
        vowel_count = sum(1 for char in password if char in vowel)
        consonant_count = L - vowel_count
        return vowel_count >= 1 and consonant_count >= 2

    for comb in combinations(alphabet, L):
        if is_valid(comb):
            print(''.join(comb))

if __name__ == "__main__":
    solution1()
    solution2()