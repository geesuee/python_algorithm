# 프로그래머스 입국심사

"""

"""

def solution(n, times):
    start, end = 1, max(times)*n
    answer = 0

    while start <= end:
        people = 0
        mid = (start + end) // 2

        for t in times:
            people += mid // t
        
        if people >= n:
            end = mid-1
        else:
            start = mid+1

    return start

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    # n = 4
    # times = [1, 1, 1]
    answer = solution(n, times)
    print(answer)