# 백준 2504번 괄호의 값

"""


"""

from sys import stdin
input = stdin.readline

def solution():
    sentence = input()
    stack = []

    answer = 0
    temp = 1
    last = ""

    for c in sentence:
        # 열린 괄호
        # - 열린 괄호가 여러 개 중첩되면 * 연산이기 떄문에 닫힐 때까지 * 연산
        if c == "(":
            stack.append(c)
            temp *= 2

        elif c == "[":
            stack.append(c)
            temp *= 3

        # 닫힌 괄호
        # - 괄호가 올바르게 닫혔는지 확인
        # - 올바르게 닫혔다면 괄호가 열려있는 동안 누적된 값을 이전 값이 + 연산
        # - 이전에 * 연산 되었던 값을 괄호 닫으면서 원복
        elif c == ")":
            if not stack or stack[-1] != "(":
                return 0
            if last == "(":
                answer += temp
            stack.pop()
            temp //= 2

        elif c == "]":
            if not stack or stack[-1] != "[":
                return 0
            if last == "[":
                answer += temp
            stack.pop()
            temp //= 3

        # 이전 값 저장
        last = c
    
    if stack:
        return 0
    else:
        return answer
           

if __name__ == "__main__":
    answer = solution()
    print(answer)