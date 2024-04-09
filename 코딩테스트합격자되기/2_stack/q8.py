# 저자 출제 문제 - 괄호 짝 맞추기

# 내 풀이
def solution(input):
    
    # 스택에 입력 값에 있는 괄호를 하나씩 add
    # 가장 최근에 넣은 괄호와 짝이 맞는 괄호가 나오면 pop
    # 입력 값을 다 처리한 뒤에, 스택에 남은 게 없으면 True, 있으면 False

    stack = []
    for char in list(input):
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    return len(stack) == 0

# 다른 사람 풀이
def soulution(input):
    stack = []

    for c in input:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            else:
                stack.pop()

    # if list => list 가 비어있지 않으면 True
    # if not list => list 가 비어있으면 True
    if stack:
        return False
    else:
        return True

if __name__ == "__main__":
    # input = "(())()"
    # input = "((())()"
    # input = ")("
    # input = ")"
    input = "("
    answer = solution(input)
    print(answer)