# 프로그래머스. N으로 표현

"""
- 5와 사칙연산만으로 12를 표현
    - 12 = 5 + 5 + (5/5) + (5/5) ⇒ 5를 6번 사용
    - 12 = 55/5 + 5/5 ⇒ 5를 5번 사용
    - 12 = (55+5) / 5 ⇒ 5를 4번 사용
- 숫자 N과 number 가 주어질 때, N과 사칙연산만 사용해서 표현할 수 있는 방법 중 N 사용 횟수의 최소값 return
- **최솟값이 8보다 크면 -1 return**
---
- N : 사용할 수 있는 숫자
- number : N을 사용하여 만들어야 하는 숫자
---
- 1 ≤ N ≤ 9
- 1 ≤ N ≤ 32,000

0. 변수 n 값 찾기
    - N을 가지고 number를 만들어야 함
    - N을 가지고 만들 수 있는 number 집합을 만들고
    - N을 2개 가지고 number를 만들 수 있는지 확인 → 있으면 해당 수에 N이 몇 개 들어갔는지 반환   
    **→ 동적 계획법에서 n이 될 변수는 N을 사용하는 횟수**
0. 점화식 찾기
    - N = 5, 5를 x개 사용하여 만들 수 있는 수 개수
        f(x) : N을, 즉 이 케이스에서는 5를 x개 사용하여 만들 수 있는 수 
        55…55 (5가 x개 들어간 수)
        + f(1) (사칙연산) f(x-1)
        + f(2) (사칙연산) f(x-2)
        + f(3) (사칙연산) f(x-3)
        …
        + f(n-1) (사칙연산) f(1)

---
1. 주어진 N을 1~8개 사용하여 만들 수 있는 수 집합을 담을 배열 생성(배열 안에 집합이 있는 구조)
    - 8개보다 더 많이 사용하면 -1 반환이니 그 전까지만 확인
2. 각 집합에 주어진 N을 1~8개 쭉 이어붙이기만 했을 때 나오는 수 추가
    - arr[1].add(int(str(N) * 1)) ⇒ N
    - arr[2].add(int(str(N) * 2)) ⇒ NN
3. 태뷸레이션으로 상향식 연산
    - 반복문으로 구현
    - 이전 연산에 사칙연산(+,-,/,*) 한 결과를 집합에 추가
4. 구하는 number가 집합에 있는지 확인
    - 있다면 해당 집합이 N을 몇 개 사용한 집합인지 인덱스로 확인 후 반환
    - 없다면 -1 반환
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