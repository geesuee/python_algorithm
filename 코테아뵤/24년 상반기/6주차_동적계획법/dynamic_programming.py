# 다이나믹 프로그래밍

# 메모이제이션
# 햐향식 방식으로 큰 값인 N부터 아래로 내려가는 방식
# 재귀로 구현
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# 태뷸레이션
# 상향식 방식으로 가장 작은 값부터 N까지 올라가는 방식
# 반복문으로 구현
def fibonacci_tab(n):
    if n <= 1:
        return n
    
    # Initialize the base cases
    table = [0] * (n + 1)
    table[1] = 1
    
    # Build the table from bottom to top
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    
    return table[n]

if __name__ == "__main__":
    print(fibonacci_memo(10))
    print(fibonacci_tab(10))