# 백준 11047번 동전 0

"""

"""

from sys import stdin
input = stdin.readline
from collections import deque

def solution():
    N, K = map(int, input().split())
    
    stack = deque()
    for _ in range(N):
        stack.append(int(input()))

    used_coin = 0
    price = K
    while stack:
        coin = stack.pop()

        if coin > price:
            continue
        
        coin_cnt = price // coin
        used_coin += coin_cnt
        price -= coin * coin_cnt

        if price == 0:
            break

    print(used_coin)

if __name__ == "__main__":
    solution()