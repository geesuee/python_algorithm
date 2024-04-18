# 프로그래머스 입국심사

"""
- n명이 입국심사를 위해 줄을 서 있음
- 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간이 다름
- 줄을 선 순서대로 빈 심사대에 가서 심사를 받음
- 모든 사람이 심사를 받는데 걸리는 시간 연산
---
- n : 입국심사를 기다리는 사람 수
- times : 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열
---
- 1 ≤ n ≤ 1,000,000,000 (10^9)
- 1 ≤ times의 한 요소 ≤ 1,000,000,000 (10^9)
- 1 ≤ len(times) ≤ 100,000 (10^5)
---
- 찾아야 할 값 : 총 시간의 최소값
- 탐색 구간 최소 값 : 1
- 탐색 구간 최대 값 : max(시간)*n


1. 최소 시간 담을 변수 생성, max 값으로 초기화
2. 이분 탐색 구현
    - 시작 : 1
    - 끝 : max(시간) * n
    - **mid 분 동안 모든 심사원이 심사할 수 있는 사람의 수 연산**
    - 심사할 수 있는 사람 수가 n 보다 크면,
        → 시간을 줄여도 됨, end = mid - 1
    - 심사할 수 있는 사람 수도 n 보다 작으면,
        → 시간을 늘려야 됨, start = mid + 1
3. 탐색 종료 후 start 출력
"""

def solution(n, times):
    start, end = 1, max(times)*n
    answer = 0

    while start <= end:
        people = 0
        mid = (start + end) // 2

        for t in times:
            people += mid // t
        
        if people >= n:
            end = mid-1
        else:
            start = mid+1

    return start

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    # n = 4
    # times = [1, 1, 1]
    answer = solution(n, times)
    print(answer)