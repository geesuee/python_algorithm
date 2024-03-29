# 프로그래머스 - 짝지어 제거하기

# 내 풀이
def solution(s):

    stack = []
    for char in s:
        # 다른 사람 풀이, 저자 풀이를 보고 나니까, 쓸데없이 분기를 너무 많이 함..
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack:
                if char == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
    
    return 0 if stack else 1

# 다른 사람 풀이
def solution(s):
    temp = ["",s[0]]
    # pop 모든 것을 다 pop 해도 마지막 것이 남도록, 맨 앞 자와 함께 공백 하나 넣어둠

    for i in s[1:]:
        if temp[-1]!=i:
            temp.append(i)
        else:
            temp.pop()

    # 디폴트로 공백을 넣어두었기 때문에 길이가 1이면 -> 1
    # 그 외의 경우, 스택에 남아있는 것이니까 -> 0
    return 1 if len(temp)==1 else 0

# 저자 풀이
def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return int(not stack)

if __name__ == "__main__":
    s = "baabaa"
    s = "cdcd"
    s = "cccc"
    answer = solution(s)
    print(answer)