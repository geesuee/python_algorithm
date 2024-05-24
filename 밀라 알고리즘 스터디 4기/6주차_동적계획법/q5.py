# 백준 11722번. 가장 긴 감소하는 부분 수열

"""

"""

from sys import stdin
input = stdin.readline

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    
    subset = [1] * N
    
    for i in range(N): # 원소 하나씩 접근
        for j in range(i): # 현재 원소 앞 원소 접근
            if A[j] > A[i]: # 앞 원소가 현재 원소보다 크면
		        # 만들 수 있는 최대 부분 수열 길이 갱신
		        # 현재 원소 포함 만들 수 있는 부분 수열 길이 vs 앞 원소 포함 길이 + 1(=현재 원소까지)
                subset[i] = max(subset[i], subset[j]+1)
    
    print(max(subset))

if __name__ == "__main__":
    solution()