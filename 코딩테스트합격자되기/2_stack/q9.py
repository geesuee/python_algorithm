# 저자 출제 문제 - 10진수를 2진수로 변환하기

# 내 풀이
def solution(input):

    stack = []
    a = input   # 몫
    b = 0   # 나머지

    # 시간 복잡도 : O(logN)
    while(a != 0):
        b = a % 2
        a = a // 2
        # print(a, b)
        stack.append(b)
    
    # 시간 복잡도 : ^2 되어서 O((logN)^2)
    answer = ""
    while(len(stack)!=0):
        temp = str(stack.pop())
        answer += temp
    return answer

# 다른 사람 풀이
def solution(decimal):
    stack = []

    # 시간 복잡도 : O(logN)
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2

    stack.reverse()
    return "".join(stack)

if __name__ == "__main__":
    input = 12345
    answer = solution(input)
    print(answer)