# 10610번 30

"""
- 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
    → 숫자를 섞는다는 게 한 자리씩 떼어서 새로운 수를 조합하는 것
    → 주어진 숫자 하나씩 조합하여 만들 수 있는 가장 큰 30의 배수 
- 30 = 2 x 3 x 5
    1. 5의 배수면, 마지막 자리가 0 or 5
    2. 2의 배수려면, 짝수여야 하기 때문에 마지막 자리가 0
    3. 3의 배수려면, 각 자리 수의 합이 3의 배수

1. 양수 N 입력 받기
2. 한 자리씩 뜯어서 배열 만들기
3. 0이 있는지 확인
    1. 없으면 바로 -1 출력
    2. 있으면, 나머지 수들의 합이 3의 배수인지 확인
        1. 3의 배수이면, 값이 큰 순으로 나열하여 출력
        2. 3의 배수가 아니면 -1 출력
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