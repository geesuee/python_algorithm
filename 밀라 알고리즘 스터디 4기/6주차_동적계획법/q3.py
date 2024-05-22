# 프로그래머스. N으로 표현

"""

"""

def solution(N, number):
    # N을 사용하여 만들 수 있는 수를 사용 횟수별로 나누어 집합으로 관리
    # 배열 인덱스 0~8까지 9개, 이 중 1~8까지 8개만 사용
    arr = [set() for _ in range(9)] 

    # 각 집합에 주어진 N을 쭉 이어붙이기만 했을 때 나오는 수 추가
    for i in range(1, 9):
        arr[i].add(int(str(N) * i))

    for i in range(1, 9):
        for j in range(i):
            for num1 in arr[j]:
                for num2 in arr[i-j]:
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)
                    if num2 != 0 and num1 % num2 == 0: # Zero Division error 고려
                        arr[i].add(num1 // num2)

        # 다음 숫자로 넘어가기 전에 만들어야 할 숫자가 집합에 있는지 확인
        if number in arr[i]:
            answer = i
            break
    else:
        answer = -1
    
    return answer

if __name__ == "__main__":
    answer = solution(6, 5)
    print(answer)