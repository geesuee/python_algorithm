# 백준 20922번. 겹치는 건 싫어

"""
- 수열 내 같은 원소가 여러 개 들어있는 것을 싫어하는 도현이
- 도현이를 위해 같은 원소가 K개 이하로 들어있는 최장 연속 부분 수열의 길이를 구하려고 함
- 100,000 이하의 양의 정수로 이루어진 길이가 N 인 수열이 주어지면,
이 수열 내에서 같은 정수를 K 개 이하로 포함한 최장 연속 부분 수열의 길이를 구해야 함
- **연속 부분 수열이란**
    - 증가 부분 수열이 아니라!!!
    - **모수열 내에서 연속해서 위치한 부분 수열을 선택하는 것**
---
- K : 같은 원소 개수 리밋
- N : 주어지는 수열의 길이
---
- 1 ≤ N ≤ 200,000
- 1 ≤ K ≤ 100
- 1 ≤ $a_i$ ≤ 100,000
---
- 시간 제한 1 초
- 메모리 제한 1,024 MB

1. 수열의 길이 N, 중복 횟수 리밋 K 입력 값 받기
2. 수열 입력 받기
3. 중복 원소가 K 개 이하로 들어가는 최장 연속 부분 수열 탐색
    1. 슬라이딩 윈도우로 배열의 특정 구간을 점차적으로 확장하면서 조건을 만족하는지 확인, 조건을 만족하는 최대 길이 탐색
    2. 처음에는 왼쪽 고정, 오른쪽을 확장하면서 원소별 빈도 확인
    3. 빈도 확인하면서 연속 위치에 있는 부분 수열을 늘려가다가 빈도가 넘어가면 왼쪽을 하나 줄이면서 빈도 조건 충족하는 부분 수열 탐색
4. 최장 연속 부분 수열 길이 출력
"""

from sys import stdin
input = stdin.readline

# 슬라이딩 윈도우로 조건 만족 LIS 탐색
def longest_subarray_with_limited_repeats(arr, k):
    count_dict = {}     # 딕셔너라에 각 원소 빈도 저장
    left = 0            # 슬라이딩 윈도우 시작, 왼쪽 고정
    max_len = 0         # 최장 길이 저장 변수

    for right in range(len(arr)):
        # 오른쪽 포인터를 확장하며 현재 원소의 등장 빈도 + 1
        count_dict[arr[right]] = count_dict.get(arr[right], 0) + 1

        # 슬라이딩 윈도우 내에서 특정 원소 빈도가 K 를 초과하면, 완쪽 포인터 이동시켜 빈도 줄이기
        while count_dict[arr[right]] > k:
            count_dict[arr[left]] -= 1
            if count_dict[arr[left]] == 0:
                del count_dict[arr[left]]
            left += 1
        
        # 현재 윈도우 길이 계산하고, 최대 길이 갱신
        max_len = max(max_len, right - left + 1)

    return max_len

def solution():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 중복 원소가 K 개 이하인 최장 연속 부분 수열 탐색
    max_len = longest_subarray_with_limited_repeats(arr, K)
    print(max_len)

if __name__ == "__main__":
    solution()