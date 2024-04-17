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

if __name__ == "__main__":
    solution()