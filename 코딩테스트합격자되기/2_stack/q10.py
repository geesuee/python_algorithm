# 프로그래머스 - 괄호 회전하기

# 내 풀이 + 저자 풀이
def solution(s):

    # 맨 앞에 있는 괄호를 뒤로 옮기고 하나씩 당기고 = 회전
    # 그 상태에서 올바른 괄호가 되는 상태인지 확인하고
    # 이 과정을 전체 길이만큼 (=한바퀴) 진행
    
    answer = 0
    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):

            # 문자열 회전을 인덱스로 구현
            c = s[(i+j) % n]

            # 열린 괄호는 스택에 적재
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            
            # 닫힌 괄호는 확인해서 pop
            else:
                if not stack:
                    break
                
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break
        
        # 파이썬 for-else 문, for 문이 다 돌고나면 동작함
        else:
            if not stack:
                answer += 1

    return answer

# 다른 사람 풀이
from collections import deque

def check(s):
    while True:
        if "()" in s: 
            s = s.replace("()","")
        elif "{}" in s: 
            s = s.replace("{}","")
        elif "[]" in s: 
            s = s.replace("[]","")
        else: 
            # s에 문자가 남아있으면 False
            # s에 문자가 없으면 True
            return False if s else True       

def solution(s):
    ans = 0
    que = deque(s)
    # 문자열 내 한글자씩 큐에 넣음

    for i in range(len(s)):
        # 큐에 하나씩 쪼개 넣은 것을 하나의 문자열로 합쳐서 체크
        if check(''.join(que)): 
            ans+=1
        # 리스트 회전 구현, 음수는 왼쪽에서 뒤로 돌리는 회전, 양수는 오른쪽에서 앞으로 돌리는 회전
        que.rotate(-1)
    return ans

if __name__ == "__main__":
    s = "[](){}"
    # s = "}]()[{"
    # s = "[)(]"
    # s = "}}}"
    answer = solution(s)
    print(answer)