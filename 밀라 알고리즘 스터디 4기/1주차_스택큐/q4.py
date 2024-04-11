# 백준 9012번 괄호

"""
- 입력 데이터가 올바른 괄호 문자열인지 아닌지 반환
- 올바른 괄호 = 열린 괄호가 모두 닫힘
    → 열리고 닫히지 않은 괄호는 스택에 넣어두고, 닫는 괄호가 등장할 때마다 pop

1. 데이터 수인 T 입력 받음
2. T개만큼 괄호 문자열 입력 받음
3. 올바른 괄호 문자열인지 판단하여 결과 출력
    1. 열린 괄호는 스택에 쌓음
    2. 닫힌 괄호가 나오면 최근 값에 열린 괄호가 있는지 봐서 pop
        1. 스택에 담긴 열린 괄호가 없는데, 닫힌 괄호가 나오면 바로 False하고 다음으로
    3. 최종적으로 스택이 다 비워졌으면 True, 아니면 False
"""

from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def checkVPS(line):
    stack = []

    for c in line:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                return "NO"
    
    if stack:
        return "NO"
    else:
        return "YES"
    
def solution():
    T = int(input())
    results = []

    for i in range(T):
        line = input()
        results.append(checkVPS(line))
    
    print("\n".join(results))

if __name__ == "__main__":
    solution()