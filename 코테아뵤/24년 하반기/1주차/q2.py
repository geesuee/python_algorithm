# 백준 20055번. 컨베이어 벨트 위 로봇

"""
- 컨베이어 벨트 구조
    - 길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있음
    - 벨트는 길이 1 간격으로 2N 개의 칸으로 나뉘어져 있음
    - 각 칸에는 1부터 2N까지 번호가 매겨져 있음
    - 벨트가 한 칸 회전하면
        - 1~2N-1 은 다음 번호 칸으로 이동
        - 2N 은 1번으로 이동
    - 각 칸의 내구도는 칸 번호가 i 일 때, $A_i$
    - 1번 칸은 올리는 위치, N번 칸은 내리는 위치
- 로봇 작동 방식
    - 로봇은 ‘올리는 위치’(=1번 칸)에만 올릴 수 있음
    - **로봇이 ‘내리는 위치’(=N번 칸)에 도달하면 즉시 내림**
    - 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있음
    - **로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도 -1**
- 해야하는 작업
    - 컨베이어 벨트를 이용해 로봇을 건너편으로 옮겨야 함
    1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있으면 이동
    이동할 수 없다면 가만히 있음
        1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없음 & 그 칸의 내구도가 1 이상
    3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
    4. 내구도가 0인 칸의 개수가 K 개 이상이라면 과정 종료. 그렇지 않다면 1번부터 다시 반복
    ⇒ 종료되었을 때 몇 번째 단계가 진행 중이었는지 구해야 함
---
- N : 컨베이어벨트 길이
- K : 내구도가 0인 칸의 개수 리밋
- $A_i$ : 각 칸의 내구도
---
- 2 ≤ N ≤ 100
- 1 ≤ K ≤ 2N
- 1 ≤ $A_i$ ≤ 1,000
---
- 시간 제한 1 초
- 메모리 제한 512 MB

1. 컨베이어 벨트 길이 N, 내구도 0인 칸 리밋 K 입력 받기
2. 벨트의 내구도 입력 받기
3. 로봇의 유무를 나타내는 배열 생성(디폴트 False)
4. 현재 단계를 저장할 변수 생성
5. 내구도가 0인 칸이 K개 이상이 될 때까지 아래 반복 실행
    1. 1단계 : 벨트 회전
        - 벨트를 회전하면서 내구성 배열도 회전 시키고
        - 로봇 위치도 한 칸 씩 회전
        **→ N 인덱스가 있으면 로봇을 내리기 때문에 해당 인덱스 삭제**
    2. 2단계 : 로봇 이동
        - 제일 먼저 올라온 = 내리는 위치에 가장 가까운 = N-1 위치부터 쭉 확인
        - 해당 위치에 로봇 있음 + 다음 자리에 로봇 없음 + 해당 위치 내구도가 1 이상 → 이동
        → 로봇이 있는 인덱스의 내구도 -1
        **→ N 인덱스가 있으면 로봇을 내리기 때문에 해당 인덱스 삭제**
    3. 3단계 : 로봇 올리기
        - 올리는 위치에 내구도가 1 이상이면 올림
        - 로봇을 올렸기 때문에 올리는 위치 내구도 -1
6. 종료 시점의 단계 출력
"""

from sys import stdin
input = stdin.readline

def rotate_belt_and_robots(N, belt, robots):
    # 벨트와 로봇 회전
    belt.insert(0, belt.pop())      # 벨트를 한 칸 회전
    robots = [False] + robots[:-1]  # 로봇 위치도 한 칸 회전

    # 내리는 위치에 로봇이 있으면 즉시 내림
    if robots[N-1]:
        robots[N-1] = False

    return robots

def move_robots(N, belt, robots):
    # 로봇 이동
    for i in range(N-2, -1, -1):    # 로봇을 내리는 위치에 가까운 순서로 이동(N-2 ~ 0, 인덱스라서 N-"2")
        if robots[i] and not robots[i+1] and belt[i+1] > 0:     # 앞에 로봇이 없고 내구도가  남아있으면 이동
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1

    # 내리는 위치에 로봇이 있으면 즉시 내림
    if robots[N-1]:
        robots[N-1] = False

    return robots, belt

def place_robot_on_belt(belt, robots):
    # 올리는 위치에 로봇 올리기
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1

    return robots, belt

def count_zero_on_belt(belt):
    # 내구도가 0인 칸의 수 반환
    return belt.count(0)


def solution():
    N, K = map(int, input().split())
    belt = list(map(int, input().split()))

    robots = [False] * N # 로봇의 위치 관리
    step = 0

    while True:
        step += 1

        # 1단계: 벨트와 로봇을 한 칸 회전
        robots = rotate_belt_and_robots(N, belt, robots)

        # 2단계: 로봇을 이동
        robots, belt = move_robots(N, belt, robots)

        # 3단계: 올리는 위치에 로봇 올리기
        robots, belt = place_robot_on_belt(belt, robots)

        # 4단계: 내구도 0인 칸이 K개 이상이면 종료
        if count_zero_on_belt(belt) >= K:
            break
    
    print(step)


if __name__ == "__main__":
    solution()