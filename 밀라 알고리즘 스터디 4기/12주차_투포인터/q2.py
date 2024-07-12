# 백준 2470번. 두 용액

"""
- 산성 용액과 알칼리성 용액이 있음
- 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어짐
- 산성 용액은 1 ~ 1,000,000,000 까지의 양의 정수로 나타내고
- 알칼리성 용약은 -1 ~ -1,000,000,000 까지의 음의 정수로 나타냄
- 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합임
- 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만드려고 함
- 두 종류의 알칼리성 용액만으로나 두 종류의 산성 용액만으로 특성값이 0에 가까운 혼합 용액을 만드는 경우도 존재할 수 있음
---
- N : 전체 용액의 수
---
- 2 < N < 100,000
- -1,000,000,000 ≤ 각 용액의 특성값 ≤ 1,000,000,000
---
- 시간 제한 1 초
- 메모리 제한 128 MB

1. 전체 용액의 수 N 입력 받기
2. N 개의 각 용액의 특성 값 입력 받아 배열에 저장
3. 용액 특성값이 담긴 배열 오름차순 정렬
4. 맨 앞을 start, 맨 뒤를 end 로 지정하고
start 값이 end 보다 커지지 않는 동안 반복문 실행
    (이중 반복문으로 모든 조합을 더하기보다 정렬한 배열에서 투 포인터로 두 용액의 특성값 합을 보면서 값을 조정해가는 방식)
    1. start 인덱스에 있는 값과 end 인덱스에 있는 값을 더함
    2. 해당 값의 절대값을 현재 min 값과 비교하여 
        1. min 보다 작으면 → min 값과 사용 용액 값 갱신
        2. 합이 0보다 크면 → end 인덱스를 -1
        3. 합이 0보다 작으면 → start 인덱스를 +1
5. 반복문에서 빠져나오면 min 값을 만드는데 사용된 용액 값을 오름차순으로 출력
"""

from sys import stdin
input = stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    start, end = 0, N-1
    min_value = float('inf')
    sol_list = []

    while start < end:
        value = arr[start] + arr[end]
        abs_value = abs(value)

        if abs_value < min_value:
            min_value = abs_value
            sol_list = [arr[start], arr[end]]

        if value > 0:
            end -= 1
        else:
            start += 1
    
    print(*sol_list)

if __name__ == "__main__":
    solution()