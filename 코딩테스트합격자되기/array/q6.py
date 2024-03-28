# 프로그래머스 - 실패율

# 내 풀이
def solution(N, stages):

    # 총 N개의 스테이지가 있음 -> 1 ~ N+1 까지 상태값 있을 수 있음
    # 전체 유저 수 파악
    # 각 스테이지에 있는 사람 파악
    # 실패율 = (해당 스테이지 유저 수) / (전체 유저 수) - (누적 이전 스테이지 유저 수)

    users = len(stages)
    users_before = 0
    fail_count_arr = [0] * N

    for i in range(N):
        on_stage_user = stages.count(i+1)
        # count로 찾는 방법 시간 복잡도가 O(N)이라서 좋은 풀이 아닌듯

        if on_stage_user == 0:
            fail_count = 0
        else:
            fail_count = on_stage_user / (users - users_before)
        
        users_before += on_stage_user
        fail_count_arr[i] = fail_count

    sorted_fail_count = sorted(list(set(fail_count_arr)), reverse=True)
    # print(sorted_fail_count)
    # print(fail_count_arr)
    # print()
    
    answer = []
    for i in sorted_fail_count:
        # print(i)
        temp_arr = []
        for j in range(len(fail_count_arr)):
            if i == fail_count_arr[j]:
                temp_arr.append(j+1)
        # print(temp_arr)
        # print()
        answer = answer + temp_arr
    
    return answer

# 다른 사람 풀이
def solution(N, stages):
    result = {}
    # 실패율을 저장하는 자료형을 배열이 아닌 딕셔너리로 지정!!!
    # 딕셔너리기 때문에 key, value를 다 저장할 수 있음
    # key에는 스테이지가, value에는 실패율 저장
    denominator = len(stages)
    # 전체 유저 수와 이전 스테이지 유저 수를 따로 변수로 선언할 필요 없음
    # 실패 율에서 분모에 들어가는 값을 변수 하나로 관리
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
    # sorted 함수에 key 값을 넣으면 변수 정렬의 기준을 명시할 수 있음
    # sorted에 딕셔너리를 넣으면, 디폴트가 key 값을 정렬 및 반환
    # 그래서 정렬 기준을 value가 되도록 바꿔주기만 하면, value 값 기준 정렬된 key 값 반환

# 다른 사람 풀이
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    # 스테이지별 유저 수 구하기
    for stage in stages:
        info[stage] += 1
    
    # 실패율 구하기
    for i in range(N):
        be = sum(info[(i + 1):])
        # be는 본 스테이지부터 다음 스테이지까지 유저 수 총합 구하는 로직
        yet = info[i + 1]
        # yet은 본 스테이지 유저

        # 2차원 배열로 실패율 값 적재
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))

    # 2차원 배열에서 실패율로 정렬하는 로직
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer

if __name__ == "__main__":
    answer = solution(5, [2,1,2,6,2,4,3,3])
    answer = solution(4, [4,4,4,4,4])
    print(answer)