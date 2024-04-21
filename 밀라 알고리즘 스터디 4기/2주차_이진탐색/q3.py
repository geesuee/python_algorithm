# 백준 18870번 좌표 압축

"""
- 수직선 위에 N개의 좌표가 있음
- 좌표를 압축한 결과를 출력해야 함
---
- 좌표 압축이란?
    - a : 원본 좌표
    - b : a 좌표를 압축한 결과
    - b = a > c 를 만족하는 **서로 다른** 좌표 c의 개수
        - ‘서로 다른’ 이 값 자체가 달라야 한다는 의미 (예제 2에서 확인)
    - 압축 결과 = 원본 좌표 보다 값이 작은 좌표의 수
---
- 입출력 예시
    - 2 4 -10 4 -9
    - 2 : 2보다 값이 작은 좌표의 수 = 2개 (-10, -9)
    - 4 : 4보다 값이 작은 좌표의 수 = 3개 (-10, -9, 2)
    - -10 : -10보다 값이 작은 좌표의 수 = 0개
    - 4 : (위와 동일)
    - -9 : -9보다 값이 작은 좌표의 수 = 1개 (-10)
---
- 1 ≤ N ≤ 1,000,000
- -10^9 ≤ X ≤ 10^9

1. 전체 좌표 개수 N 입력 값 받기
2. 좌표 리스트 입력 값 받기
3. 원 리스트를 두고, 별도의 복제 리스트를 unique 처리
4. unique 된 리스트를 정렬 - O(NlogN)
5. 요소를 key, 정렬된 index를 value로 딕셔너리 생성
6. 원 리스트 한 요소씩 반복문으로 접근
    1. 요소를 키 값으로 정렬된 index 접근, 출력
"""

from sys import stdin
input = stdin.readline

def solution():
    N = int(input())
    dot_list = list(map(int, input().split()))
    dot_dict = {v:i for i, v in enumerate(sorted(set(dot_list.copy())))}
    
    for dot in dot_list:
        print(dot_dict.get(dot), end=" ")

# 만약 '서로 다른' 조건이 없다면,
# 예제 1 변형) 2 4 -10 4 5 -9 -> 0 1 2 3 3 5
# 예제 2) 1000 999 1000 999 1000 999 -> 3 0 3 0 3 0

from collections import Counter

def find_big_idx_than(dict, a):
    result = {}
    for key, value in dict.items():
        if key > a:
            result[key] = value
    return result

def solution():
    N = int(input())
    dot_list = list(map(int, input().split()))
    dot_dict = {v:i for i, v in enumerate(sorted(set(dot_list.copy())))}
    dot_dict_reverse = {v:k for k,v in dot_dict.items()}
    dot_counter = Counter(dot_list)

    for dot in dot_counter:
        if dot_counter[dot] > 1:
            dot_idx = dot_dict[dot]
            update_need_dot_dict = find_big_idx_than(dot_dict_reverse, dot_idx)
            for key_idx, val_num in update_need_dot_dict.items():
                dot_dict[val_num] += dot_counter[dot]-1
    
    for dot in dot_list:
        print(dot_dict.get(dot), end=" ")

if __name__ == "__main__":
    solution()