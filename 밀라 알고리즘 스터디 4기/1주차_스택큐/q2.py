# 백준 1158번 요세푸스 문제

"""
- 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고 → 큐 활용   
- 양의 정수 K가 주어진다. 순서대로 K번째 사람을 제거한다. → 제거하는 사람은 빼고, 넘어가는 사람은 뒤로 넘기고
- 모든 사람이 제거될 때까지 반복
- 원에서 사람들이 제거되는 순서 = (N, K)-요세푸스 순열 구하는 프로그램 작성

1. 1부터 N까지 값이 들어간 큐 생성
2. 큐에 값이 남아있는 동안
    1. K번째 값이 나올 때까지 값을 빼서 다시 뒤로 넣고
    2. K번째 값이 나오면, 해당 값을 answer 리스트에 넣음
3. answer 리스트 출력
"""

# 내 풀이
from sys import stdin, stdout
from collections import deque
input = stdin.readline
print = stdout.write

def solution():

    N, K = map(int, input().split())
    q = deque()
    answer = []

    for i in range(N):
        q.append(str(i+1))
    
    while q:
        for i in range(K):
            if i == K-1:
                answer.append(q.popleft())
            else:
                q.rotate(-1)
    
    answer_str = ", ".join(answer)
    answer_str = "<" + answer_str + ">"
    print(answer_str)

# 개선한 풀이
from sys import stdin, stdout
from collections import deque
input = stdin.readline
print = stdout.write

def solution():

    N, K = map(int, input().split())
    stack = [str(i) for i in range(1, N+1)]
    answer = []

    idx = 0
    while stack:
        idx = (idx+K-1) % len(stack)
        answer.append(stack.pop(idx))
    
    answer_str = ", ".join(answer)
    answer_str = "<" + answer_str + ">"
    print(answer_str)

if __name__ == "__main__":
    solution()

