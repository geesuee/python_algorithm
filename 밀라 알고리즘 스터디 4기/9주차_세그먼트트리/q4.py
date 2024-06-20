# 백준 3020번. 개똥벌레

"""
- 개똥벌레 한 마리가 장애물이 있는 동굴에 들어감
- 동굴의 길이는 N 미터, 높이는 H 미터
- 첫 번째 장애물은 항상 석순, 그 다음에는 종유석과 석순이 번갈아 등장
- 개똥벌레는 장애물을 피하지 않고, 
지나갈 구간을 정해서 일직선으로 지나가면서 만나는 모든 장애물을 파괴함
- 개똥벌레가 파괴해야하는 `장애물의 최솟값`과 그러한 `구간이 몇 개` 있는지 공백으로 구분하여 출력
---
- N : 동굴의 길이
- H : 동굴의 높이
- $n_i$ : 장애물의 크기 (장애물은 총 N 개)
---
- 2 ≤ N ≤ 2*$10^5$
- 2 ≤ H ≤ 5*$10^5$
- 1 ≤ $n_i$ < H
---
- 시간 제한 1 초
- 메모리 제한 128 MB
---
- 입출력 예시 
    길이(N) 14, 높이(H) 5인 동굴
    | 날아가는 높이 | 부딛히는 석순 수 | 부딛히는 종유석 수 | 총 장애물 수 | 최소 장애물 여부 |
    | --- | --- | --- | --- | --- |
    | 1 | 7 | 0 | 7 | O |
    | 2 | 6 | 2 | 8 |  |
    | 3 | 5 | 4 | 9 |  |
    | 4 | 1 | 7 | 8 |  |
    | 5 | 0 | 7 | 7 | O |
    - 개똥벌레가 날아가는 높이별로 그 높이보다 큰 장애물이 몇 개나 있는지를 파악해야 함
    - 누적 합을 통해, 각 높이를 기준으로 파괴되는 장애물의 개수를 연산
        - 석순의 높이가 1, 5, 2, 3, 3, 3, 3 일 때
        - 높이 1로 날면 잘리는 석순 7개 (1보다 큰 값의 개수)
        - 높이 2로 날면 잘리는 석순 6개 (2보다 큰 값의 개수)
        → 석순의 높이 별로 몇 개가 있는지 저장해두고
        **→ 높은 레벨부터 낮은 레벨로 가면서 몇 개가 잘리는 지 연산, 이전 값 누적하여 합산
        (작은 레벨로 날 때는 그것보다 큰 레벨에서 잘렸던 것들은 무조건 잘리기 때문에)**

1. 동굴의 길이 N, 높이 H 입력 받음
2. N 개 만큼 장애물의 크기 입력 받음
    1. 맨 앞은 석순, 다음은 종유석
    2. 석순과 종유석을 나누어 각각 배열에 높이 몇 짜리가 몇 개 있는지 입력 받음
3. 장애물 누적합 연산
    1. 가장 높은 높이에서부터 낮은 높이로 역순으로 돌면서
    2. 높은 곳에서 잘린 건, 낮은 곳에서도 무조건 잘린다 → 누적합 연산
4.  높이 1에서부터 H까지 돌면서, 어디로 날 때 잘리는 장애물이 제일 적은지, 그 구간이 몇 개인지 연산
    1. 기존 min 보다 작은 값이 나오면 → 갱신하고 구간 개수는 1로 초기화
    2. 기존 min 과 같은 값이 나오면 → 구간 개수 + 1
"""

from sys import stdin
input = stdin.readline

def solution():
    N, H = map(int, input().split())

    # 높이별 장애물이 몇 개 있는지 저장할 배열
    down = [0] * (H+1)  # 석순
    up = [0] * (H+1)    # 종유석
    
    # 높이별 장애물 개수 파악
    for i in range(N):
        size = int(input())

        # 0부터 시작하니까 짝수번째가 석순
        if i % 2 == 0: 
            down[size] += 1
        else:
            up[size] += 1 

    # 높은 레벨 -> 낮은 레벨, 잘리는 장애물 수 누적 합 연산
    for i in range(H-1, 0, -1): # H-1 ~ 1, 장애물은 H 보다 작음
        # 더 큰 레벨 값을 작은 레벨 값에 합산
        down[i] += down[i+1]
        up[i] += up[i+1]
    
    # 최소 값, 구간 개수 확인
    min_cnt = N
    h_cnt = 0
    for i in range(1, H+1): # 1 ~ H
        # 레벨 2일 때, 
        # 석순은 레벨 2 그대로 확인하면 되지만
        # 종유석에서 레벨 1은 천장에서부터라 사실 상 H-2+1
        break_cnt = down[i] + up[H-i+1]
        
        # 갱신
        if break_cnt < min_cnt:
            min_cnt = break_cnt
            h_cnt = 1
        
        # 구간 추가
        elif break_cnt == min_cnt:
            h_cnt += 1
    
    print(min_cnt, h_cnt)

if __name__ == "__main__":
    solution()