# 백준 11399번. ATM

"""
- ATM 앞에 N 명의 사람들이 줄을 서있다.
- 사람은 1번부터 N번까지 번호가 매겨져 있으며
- i번 사람이 돈을 인출하는데 걸리는 시간은 Pi 분이다.
- 줄을 서 있는 사람 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 P가 주어졌을 때, 각 사람이 **돈을 인출하는데 필요한 시간 합의 최솟값 연산**
- 앞 사람의 인출 시간이 뒷 사람의 총 대기 시간에 포함되기 때문에
인출 시간이 적은 순으로 정렬하여 처리해야 합이 최솟값이 됨
    → 그리디
---
- N : 사람의 수
- P : 각 사람이 돈을 인출하는데 걸리는 시간
---
- 1 ≤ N ≤ 1,000
- 1 ≤ P ≤ 1,000

1. 사람의 수 N 입력 받기
2. 돈을 인출하는데 걸리는 시간 P 배열 입력 받기
3. 인출 시간 배열 오름차순 정렬
4. 누적 소요 시간 변수 생성 및 0으로 초기화
5. 정렬된 배열 내 값 반복문으로 접근
    1. 누적 시간 += P[i] * (배열 길이 - i)
6. 누적 시간 값 출력
"""

from sys import stdin
input = stdin.readline

def solution():
    N = int(input())
    P = list(map(int, input().split()))
    
    P.sort()

    total_time = 0
    p_len = len(P)  # 매번 새로 연산하지 않고 한 번 연산해서 재사용
    for i in range(p_len):
        total_time += P[i] * (p_len-i)
    
    print(total_time)

if __name__ == "__main__":
    solution()