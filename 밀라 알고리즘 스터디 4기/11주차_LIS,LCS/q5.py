# 백준 7453번. 합이 0인 네 정수
# LIS, LCS 아닌 랜덤 문제

"""
- 정수로 이루어진 크기가 같은 배열 A, B, C, D
- A[a], B[b], C[c], D[d] 의 합이 0인 (a, b, c, d) 쌍의 개수를 구해야 함
---
- n : 배열의 크기
---
- 1 ≤ n ≤ 4,000
- $-2^{28}$ ≤ 배열 내 원소 ≤ $2^{28}$
---
- 시간 제한 12 초
- 메모리 제한 1024 MB

- 4중 반복문으로 값 하나씩 접근하여 연산할 경우,
    - 배열의 크기가 최대 4,000
    - 최대 시간 복잡도는 O(4,000 * 4,000 * 4,000 * 4,000)
    = $O(4^4*10^{12})$
    - 시간 제한 왜 12 초나 주는거지..? 이 풀이로는 안될 것 같은데…
- 다른 방식
    - A, B, C, D 에서 하나씩 뽑아서 합산하는 것을 여러 번 테스트 해야함
    - 그 중에 중복되는 연산이 있을 것, 중복되는 연산은 저장해두고 다시 사용
    - A, B 각 원소를 더한 합을 싹 저장 해놓고
    C, D 각 원소를 더합 합을 싹 저장 해놓고
    → 두 개를 더해서 0이 되는 **조합의 개수 찾기**
    - 개수를 찾아야 하니까 합으로 만들어진 수를 key 로 해당 개수를 만들 수 있는 조합을 value 로 딕셔너리에 저장
---
1. A, B, C, D 배열 생성
2. 배열 길이 n 입력 받기
3. 원소 값 입력 받기
4. A 와 B 를 더한 조합 연산하여 딕셔너리에 저장
5. C 와 D 를 더한 조합을 찾고, A, B 조합과 합하여 0이 되는 개수 파악
6. 총 합이 0 이 되는 개수 출력
"""

# 시간 초과 💥
from sys import stdin
input = stdin.readline

def solution():
    A, B, C, D = [], [], [], []
    answer = 0

    N = int(input())
    for _ in range(N):
        a, b, c, d = map(int, input().split()) 
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)   
    
    ab = dict()
    for a in A:
        for b in B:
            value = a + b
            if value in ab.keys():
                ab[value] += 1
            else:
                ab[value] = 1
    
    for c in C:
        for d in D:
            value = c + d
            if -value in ab.keys():
                answer += ab[-value]

    print(answer)

if __name__ == "__main__":
    solution()