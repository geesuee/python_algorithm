# 백준 1931번 회의실 배정

"""
- 한 개의 회의실, 회의실을 사용하고자 하는 N개의 회의
- 각 회의 i 에 대해 시작시간과 끝나는 시간이 주어짐
- 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 **최대 개수**
    → 겹치는 구간이 있다면 더 많은 회의가 진행될 수 있도록
---
- N : 회의의 수
- 각 회의는 시작 시간, 끝나는 시간 존재
- 시작 시간 == 끝나는 시간일 수 있음
---
- 1 ≤ N ≤ 100,000
- 0 ≤ 시간 < 2^31-1

1. N 입력 값 받기
2. N개 회의의 시작 시간, 종료 시간 입력 값 받기
3. 종료 시간을 기준으로 정렬
4. 회의 리스트를 반복문으로 하나씩 접근
    1. 예약 가능 시간(초기값=0) 보다 시작 시간이 나중이면 회의 할당
    2. 해당 회의의 종료 시간을 예약 가능 시간으로 설정
    3. 회의실에 회의를 할당할 때마다 회의 개수 변수 +1
5. 회의 개수 변수 출력
"""

from sys import stdin
input = stdin.readline

def solution():
    N = int(input())

    meeting_list = []
    for _ in range(N):
        st, ed = map(int, input().split())
        meeting_list.append((st, ed))
    
    meeting_list.sort(key=lambda x: (x[1], x[0]))

    meeting_count = 0
    st_available = 0
    for st, ed in meeting_list:
        if st >= st_available:
            meeting_count += 1
            st_available = ed
    
    print(meeting_count)

if __name__ == "__main__":
    solution()