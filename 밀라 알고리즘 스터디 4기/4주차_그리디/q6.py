# 10610번 30

"""

"""

from sys import stdin
input = stdin.readline

def solution():
    N = int(input())
    number = list(map(int, str(N)))

    if 0 not in number:
        return -1
    
    if sum(number)%3 == 0:
        return ''.join(str(x) for x in sorted(number, reverse=True))
    else:
        return -1

if __name__ == "__main__":
    print(solution())