# 백준 6987번. 월드컵

"""

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
