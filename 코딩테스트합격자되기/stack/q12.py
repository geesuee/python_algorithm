# 프로그래머스 - 주식 가격

# 내 풀이 + 저자 풀이
def solution(prices):
    n = len(prices)
    answer = [0] * n    # 가격이 떨어지지 않은 기간을 저장할 배열

    # 스택을 사용해 이전 가격과 현재 가격 비교
    stack = [0] # 스택 초기화
    for i in range(1, n):
        # 스택이 채워져있고, 가격이 떨어진 경우
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()     # 이전 인덱스 팝
            answer[j] = i - j   # 현재 인덱스 - 팝한 인덱스 = 이전 가격의 기간 계산
        
        # 가격이 떨어지지 않은 경우
        stack.append(i)
    
    # 스택에 남아있는 인덱스는 가격이 끝까지 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    answer = solution(prices)
    print(answer)