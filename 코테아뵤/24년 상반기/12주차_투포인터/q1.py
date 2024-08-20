# 백준 2531번. 회전 초밥

"""
- 회전하는 벨트 위에 여러 가지 종류의 초밥이 접시에 담겨 있고
- 손님은 이 중에서 자기가 좋아하는 초밥을 골라서 먹음
- 초밥의 종류는 번호로 표현
- 벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있음
- `행사` 벨트의 임의의 한 위치부터 k 개 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
- `행사` 각 고객에게 초밥 종류 하나가 쓰인 쿠폰을 발행하고, 위 행사에 참여할 경우 이 쿠폰에 적힌 종류의 초밥 하나를 추가로 무료 제공(벨트 위에 없을 경우, 새로 만들어서 제공)
- 위 행사에 참여하여 가능한 다양한 종류의 초밥을 먹으려고 함
- 회전 초밥 음식점 벨트 상태, 메뉴에 있는 초밥의 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호가 주어졌을 때
손님이 **먹을 수 있는 초밥 가짓수의 최댓값**을 구해야 함
---
- N : 회전 초밥 벨트에 놓인 접시의 수
- d : 초밥의 가짓수
- k : 연속해서 먹는 접시의 수
- c : 쿠폰 번호
---
- 2 ≤ N ≤ 30,000
- 2 ≤ d ≤ 3,000
- 2 ≤ k ≤ 3,000 (k ≤ N)
- 1 ≤ c ≤ d

1. 회전 초밥 접시 수 N, 초밥 가짓수 d, 연속해서 먹는 접시 수 k, 쿠폰 번호 c 입력 받기
2. 덱을 만들어 N 개의 초밥 종류 번호 입력 받기
3. 회전초밥 벨트를 돌면서 원소에 접근
    1. 덱을 하나 더 만들어서 k 개 만큼을 순서대로 뽑아서 새 덱에 옮김
    2. 덱에 있는 값을 4 방식으로 확인하고, 다음으로 넘어갈 때
        1. 맨 앞에 있는 값을 pop 해서 기존 덱에 넣고
        2. 기존 덱에 있는 맨 앞에 있는 값을 뽑아서 새로운 덱에 넣음
        3. 이 방식으로 확인하는 원소들을 순환하여 접근
4. 확인할 값이 들어있는 덱 원소 확인
    1. 쿠폰 번호 c 가 있으면, 해당 원소 중복 제거 개수 확인
    2. 쿠폰 번호 c 가 없으면, 해당 원소를 중복 제거해서 개수 확인하고 + 1 (쿠폰)
    3. max 값을 계속 갱신함
"""

from sys import stdin
input = stdin.readline
from collections import deque

def solution():
    N, d, k, c = map(int, input().split())
    
    belt = deque()
    check = deque()

    for _ in range(N):
        dish = int(input())
        belt.append(dish)
    
    max_dish = 0
    for _ in range(N):
        # 초기 설정 : k 개 만큼 확인할 덱에 이동
        if not check:
            for _ in range(k):
                dish = belt.popleft()
                check.append(dish)
        
        # 덱 안에 쿠폰 번호 c 가 있는지 확인
        check_set = set(check)
        if c in check_set:
            curr_dish = len(check_set)
        else:
            curr_dish = len(check_set) + 1
        
        # 최댓값 갱신
        if curr_dish > max_dish:
            max_dish = curr_dish
        
        # 순환
        checked_dish = check.popleft()
        belt.append(checked_dish)
        new_dish = belt.popleft()
        check.append(new_dish)
    
    print(max_dish)
    

if __name__ == "__main__":
    solution()