# 백준 6987번. 월드컵

"""
- 승, 무승부, 패의 수가 가능한 결과인지 판별
- 가능한 결과면 1, 불가능한 결과면 0 출력
---
- 확인 조건
    - 한 국가가 치룬 경기 수의 합 = 5
    - 전체 승의 합 = 전체 패의 합
    - 무승부가 있는 나라의 수가 짝수고, 전체 합도 짝수

1. 총 네 번 한 줄씩 입력값 받기
2. 세개씩 끊어서 배열 생성, 한 줄이 한 배열로 들어가도록 → 이차원 배열
3. 이차원 배열 하나씩 반복문 실행
    1. 승패 가능 확인 로직 실행
        1. 이차원 배열 내부 원소 반복문 실행
        2. 0번째 원소 합 연산 = 승 수 합
        3. 1번째 원소가 0보다 큰 개수 연산 = 무승부 국가 수 연산
        4. 1번째 원소 합 연산 = 무승부 수 합
        5. 2번째 원소 합 연산 = 패 수 합
        
        → 승 수 합 = 패 수 합 확인
        
        → 무승부 국가 수 짝수 확인
        
        → 무승부 수 합 짝수 확인
        
        위 3개 조건 중 하나라도 부합하지 않을 시 바로 0 출력 후 break
-> 틀림ㅠㅠ
"""

from sys import stdin
input = stdin.readline
from itertools import combinations

# 내 틀린 풀이ㅠ
def check(binary_arr):
    win = 0 
    lose = 0
    draw = 0
    draw_country = 0

    for arr in binary_arr:
        win += arr[0]
        draw += arr[1]
        lose += arr[2]
        if arr[1] > 0:
            draw_country += 1
        
        sum_arr = sum(arr)
        if sum_arr != 5:
            print(0)
            return

    if win != lose:
        print(0)
        return
        
    if draw_country % 2 != 0:
        print(0)
        return

    if draw % 2 != 0:
        print(0)
        return

    print(1)
    return

def solution():
    for _ in range(4):
        temp = list(map(int, input().split()))
        res = [temp[i:i+3] for i in range(0, 16, 3)]
        
        # 승패 가능 확인 로직 실행
        check(res)        

# 다른 사람 풀이
# 백트래킹
def backtracking(depth, games, res):
    # 15번째 경기에 도달했을 때
    if depth == 15:
        for sub in res:
            # 전체 승무패의 합계가 0이 아니면
            if sub.count(0) != 3:
                return 0
        return 1
    
    # 전체 경기 15번의 조합
    g1, g2 = games[depth]
    # 각 경기의 승무패
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[g1][x] > 0 and res[g2][y] > 0:
            res[g1][x] -= 1
            res[g2][y] -= 1
            if backtracking(depth + 1, games, res):
                return 1
            res[g1][x] += 1
            res[g2][y] += 1
    return 0

def solution():
    answers = []
    games = list(combinations(range(6), 2))

    for _ in range(4):
        tmp = list(map(int, input().split()))
        res = [tmp[i:i + 3] for i in range(0, 16, 3)]
        result = backtracking(0, games, res)
        answers.append(result)
        
    print(*answers)

if __name__ == "__main__":
    solution()
