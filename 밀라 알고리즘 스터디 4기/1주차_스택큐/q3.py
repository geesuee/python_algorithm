# 프로그래머스 다리를 지나는 트럭

"""
- 트럭 여러 대가 다리를 정해진 순으로 건넘 -> 순서대로 처리, 큐 활용
- 다리에는 트럭이 최대 bridge_length대 올라감 -> 다리가 되는 큐의 길이
- 다리는 weight 이하의 무게를 견딜 수 있음 -> 큐 삽입, 삭제 시 고려해야할 조건
- 모든 트럭이 다리를 건너는데 걸리는 시간 연산

1. 다리 길이만큼 큐 생성
2. 트럭을 하나씩 돌면서
    1. 삽입 조건을 충족하면 → 트럭 삽입
    2. 충족하지 않으면 → 기존에 있는 트럭 위치만 변경
        1. 마지막 트럭을 올리고 나서,
        **총 시간에 마지막 트럭이 다리 길이만큼 이동하는 시간 추가**
    3. 누적 시간 += 1
"""

# 내 풀이
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    curr_weight = 0
    answer = 0

    while trucks:
        print(answer, curr_weight, bridge, trucks)
        # 시작하면 시간 1초 가고, 다리 위 트럭 한 칸씩 이동
        answer += 1
        curr_weight -= bridge.popleft()
        curr_truck = trucks[0]
        
        # 트럭을 올릴 수 있으면 -> 올리고 현재 무게 연산
        if curr_weight + curr_truck <= weight:
            curr_weight += curr_truck
            bridge.append(trucks.popleft())
        
        # 없으면 -> 트럭 한 칸씩 이동
        else:
            bridge.append(0)
    
    # 마지막 남은 트럭이 다리 끝까지 이동하는 시간 합산
    answer += bridge_length
    
    return answer

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]

    # bridge_length = 100
    # weight = 100
    # truck_weights = [10]

    # bridge_length = 100
    # weight = 100
    # truck_weights = [10,10,10,10,10,10,10,10,10,10]

    answer = solution(bridge_length, weight, truck_weights)
    print(answer)
    

    

        