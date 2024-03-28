# 프로그래머스 - 방문 길이

# 내 풀이
def solution(dirs):
    # U 위 Y+1
    # D 아래 Y-1
    # L 왼쪽 X-1
    # R 오른쪽 X+1
    # 0,0에서 출발해서 이동
    # 이동하는 명령어에 따라 위치 x,y 값이 바뀜
    # 이동한 경로를 저장, 중복 제거
    # 결과 위치의 절대값이 5를 넘어가면 무효

    path = set()
    # 리스트에 담았다가 중복 제거 할 필요 없이, 처음부터 중복 데이터 안들어가는 set() 사용
    x, y = 0, 0

    for dir in dirs:
        print(dir, x, y)
        if dir == "U":
            nx, ny = x, y+1
        elif dir == "D":
            nx, ny = x, y-1
        elif dir == "L":
            nx, ny = x-1, y
        elif dir == "R":
            nx, ny = x+1, y

        if (abs(nx) > 5) | (abs(ny) > 5):
            continue
        
        # print(nx, ny)
        path.add((x, y, nx, ny))
        path.add((nx, ny, x, y))

        x, y = nx, ny

    print(path)
    answer = len(path)/2
    
    return answer

# 다른 사람 풀이
def solution(dirs):
    s = set()
    # 명령어에 따른 x, y 이동을 딕셔너리에 넣어 표현
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + d[dir][0], y + d[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2

if __name__ == "__main__":
    # dirs = "ULURRDLLU"
    # dirs = "LULLLLLLU"
    dirs = "ULURRDLDL"
    answer = solution(dirs=dirs)
    print(answer)