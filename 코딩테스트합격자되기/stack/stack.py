# 스택 구현하기
# 파이썬 리스트는 크기를 동적으로 관리하기 때문에 max_size, isFull(), isEmpty() 함수를 꼭 구현할 필요는 없음 (개념 상 구현)
# push 함수 내부 로직에 append() 호출만 있어서 따로 구현하지 않고 append() 그대로 써도 됨
# pop 함수 내부 로직에 pop() 호출만 있어서 따로 구현하지 않고 pop() 그대로 써도 됨
# 스택 자체가 어렵지는 않지만, 문제에서 스택을 써야겠다 생각하는 것이 어려움 -> 많이 연습!

stack = []  # 배열로 스택 초기화
max_size = 10   # 스택 최대 크기

def isFull(stack):
    return len(stack) == max_size

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    if isFull(stack):
        print("스택이 가득 찼습니다.")
    else:
        stack.append(item)
        print("데이터가 추가되었습니다.")

def pop(stack):
    if isEmpty(stack):
        print("스택이 비어 있습니다.")
        return None
    else:
        return stack.pop()