# 백준 2805번 나무 자르기

"""
- 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.
- 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
    → 찾는 값은 절단기 높이 H
    → 최소 1에서부터, 가장 큰 나무 길이까지 중에서 탐색
    → 이진 탐색으로 구간을 반으로 줄여 나가며 탐색

1. 나무 수 N과, 필요한 나무 길이 M 입력 값 받기
2. 나무 높이 입력 값 받기
3. 나무 높이 리스트 정렬
4. 이진 탐색 구현
    1. 첫 탐색 구간은 1 ~ max(나무) 
    2. 첫 H 값은 구간 내 중간 값 (start+end)//2
    3. 나무 리스트 돌면서 H 값보다 큰 경우, 잘린 나무 길이 총합 연산
    4. 총합이 M보다 크거나 같으면, H를 더 크게 바꿔야 함 → 구간을 mid+1 ~ end
    5. 작으면, H를 더 작게 바꿔야 함 → 구간을 start ~ mid-1
"""

from sys import stdin
input = stdin.readline

def solution():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    
    start, end = 1, max(trees)

    while start <= end:
        cut_total = 0
        mid = (start + end) // 2

        # 잘린 나무 총합 연산
        for t in trees:
            if t > mid:
                cut_total += t - mid
        
        # 이진 탐색
        if cut_total == M:
            print(mid)
            break

        if cut_total >= M:
            start = mid + 1
        else:
            end = mid - 1

if __name__ == "__main__":
    solution()