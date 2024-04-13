# 백준 1966번 프린터 큐

"""
- Queue의 가장 앞에 있는 문서의 중요도 확인
    → 중요도는 숫자 크기  
    → 큐 내 max 값이 가장 우선순위 높음
- 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
    → 현재 원소가 max 값인지 아닌지 확인
    - 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치
    - 그렇지 않다면 바로 인쇄
- 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것
    → 요소 값(중요도)와 인덱스를 둘 다 고려한 연산 필요
"""

from sys import stdin, stdout
input = stdin.readline
from collections import deque


def solution():
    T = int(input())

    for _ in range(T):
        # N 문서 개수, M 추적 인덱스
        N, M = map(int, input().split())
        # 큐
        q = deque(list(map(int, input().split())))
        # 추적 인덱스 M의 출력 순서
        answer = 0

        while q:
            priority = max(q)   # 우선 순위가 제일 높은 요소
            now = q.popleft()   # 현재 맨 앞 요소
            M -= 1              # 하나 뽑아서 타겟 인덱스 당겨짐

            # 뒤에 우선순위 높은 게 없으면 -> 그대로 pop
            if now == priority:
                answer += 1     # 출력 할 때 마다 출력 순서 + 1
                if M < 0:       # 위에서 미리 타겟 인덱스 하나씩 당겼기 때문에 0보다 작을 때, 현재 값이 타겟
                    print(answer)
                    break
            
            # 있으면 -> 맨 뒤에 push
            else:
                q.append(now)
                if M < 0:       # 타겟이 뒤로 밀려서 새로운 인덱스 연산
                    M = len(q) - 1


if __name__ == "__main__":
    solution()