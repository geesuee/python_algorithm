# 백준 2875번 대회 or 인턴

"""
- 대회에 나갈 때 2명의 여학생과 1명의 남학생이 팀을 결성해야 함
- N명의 여학생과 M명의 남학생이 팀원을 찾고 있음
- K명은 반드시 인턴쉽 프로그램에 참여, 인턴쉽에 참여하면 대회에 참여하지 못함
- **최대한 많은 팀을 만들어야 함**
---
- N : 여학생 수
- M : 남학생 수
- K : 인턴쉽 참여 인원
---
- 0 ≤ N ≤ 100
- 0 ≤ M ≤ 100
- 0 ≤ K ≤ M+N

1. N, M, K 입력 값 받기
2. 여학생으로 만들 수 있는 최대 팀 수 구하기 (2명씩 팀)
3. 남학생으로 만들 수 있는 최대 팀 수 구하기 (1명씩이라 M 그대로)
4. 두 값 비교하여 더 작은 값이 만들 수 있는 최대 팀
5. 남은 여학생 수, 남학생 수 확인
6. K 로 인해 쪼개져야 하는 팀 수 확인
    1. 남은 남여 학생 수가 K보다 많으면, 초기 최대 팀 유지
    2. 적으면, 몇 팀을 쪼개야 하는 지 확인(한 팀은 3명)
"""

from sys import stdin
input = stdin.readline
import math

# 내 풀이
def solution():
    N, M, K = map(int, input().split())

    max_team = min(N//2, M)
    leaft_girl_boy = (N - 2*max_team) + M - max_team

    need = K - leaft_girl_boy
    if need > 0:
        max_team -= math.ceil(need/3)

    print(max_team)

# 백준 다른 사람 풀이
def solution():
    n, m, k = map(int, input().split())
    print(min((n+m-k)//3, n//2, m))

if __name__ == "__main__":
    solution()