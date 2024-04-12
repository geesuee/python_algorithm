# 백준 9093번 단어 뒤집기

"""
- 단어를 모두 뒤집어서 출력
    → 단어 회전
    → reverse(), rotate() 함수 시간 복잡도 O(N)
    → 실제로 회전 시키지 말고 **인덱스로 접근**

1. 테스트 케이스 개수 입력
2. 테스트 케이스 개수를 기준으로 반복문 실행
    1. 문장 입력
    2. 단어 하나씩 회전
    3. 리스트에 추가
    4. join으로 간격 추가하여 문장으로 출력
"""

from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def solution():
    T = int(input())

    for _ in range(T):
        words = input().rstrip().split()

        reverse_words = []
        for w in words:
            reverse_words.append(w[::-1])
    
        answer = " ".join(reverse_words)
        print(answer+"\n")

if __name__ == "__main__":
    solution()