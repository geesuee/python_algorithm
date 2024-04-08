# 백준 10829번 스택

"""
단순 스택 구현 문제

1. 스택 클래스 생성, 명령 처리 함수 구현
2. 명령 수 N으로 반복문 만들어 명령 처리하는 로직 진행
    1. 명령어 only
        - pop : pop하고 출력, 스택이 비어있는 경우 -1 출력
        - size : 스택 사이즈 출력
        - empty : 스택이 비어있으면 1, 아니면 0
        - top : peek하고 출력, 스택이 비어있는 경우 -1 출력
    2. 명령어 + 숫자
        - push : 주어진 수를 스택에 추가
"""

# 스택 클래스 사용 O
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return 0 if self.stack else 1
    
    def size(self):
        return len(self.stack)

    def push(self, X):
        self.stack.append(X)
    
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.stack.pop() 
    
    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]

def solution():
    stack = Stack()

    N = int(input())

    for _ in range(N):
        command = input().rstrip()

        if command == "pop":
            print(str(stack.pop())+"\n")

        elif command == "size":
            print(str(stack.size())+"\n")

        elif command == "empty":
            print(str(stack.empty())+"\n")

        elif command == "top":
            print(str(stack.top())+"\n")

        elif command[:4] == "push":
            X = command.split()[1]
            stack.push(X)

# 스택 클래스 사용 X
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def solution():
    stack = []

    N = int(input())
    
    answer_list = []
    for _ in range(N):
        command = input().rstrip()

        if command == "pop":
            answer_list.append(stack.pop() if stack else "-1")

        elif command == "size":
            answer_list.append(str(len(stack)))

        elif command == "empty":
            answer_list.append("0" if stack else "1")

        elif command == "top":
            answer_list.append(stack[-1] if stack else "-1")

        elif command[:4] == "push":
            X = command.split()[1]
            stack.append(X)
            
    answer_str = "\n".join(answer_list)
    print(answer_str)


if __name__ == "__main__":
    solution()