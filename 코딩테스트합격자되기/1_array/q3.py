# 프로그래머스 - 두 개 뽑아서 더하기

# 내 풀이
def solution(numbers):
    # numbers 에 있는 숫자로 만들 수 있는 숫자 합 하나씩 구하고
    # 중복 제거
    # 정렬

    answer = set()
    for i in range(len(numbers)):
        # 앞에서부터 하나씩 확인하니까 다시 뒤로 확인할 필요는 없음
        # 두번째 반복문은 i+1 부터 돌도록 설정
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
        
    return sorted(list(answer))

if __name__ == "__main__":
    # numbers = [2,1,3,4,1]
    numbers = [5,0,2,7]
    answer = solution(numbers=numbers)
    print(answer)