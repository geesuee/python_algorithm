# 프로그래머스 - 모의고사

# 내 풀이
def solution(answers):

    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    score = [0,0,0]
    for i in range(len(answers)):
        ans = answers[i]

        if (ans == patterns[0][i%5]):
            score[0] += 1
        
        if (ans == patterns[1][i%8]):
            score[1] += 1

        if (ans == patterns[2][i%10]):
            score[2] += 1

    max_score = max(score)
    print(max_score)

    answer = []
    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)

    return answer

# 다른 사람 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    # enumerate 함수를 사용하면 인덱스와 값을 함께 들고 반복문 돌 수 있음
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

if __name__ == "__main__":
    # answers = [1,2,3,4,5]
    answers = [1,3,2,4,2]
    answer = solution(answers=answers)
    print(answer)