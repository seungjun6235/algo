import sys
sys.stdin = open('input.txt')

def my_reverse(line):
    r_line = []
    for i in range(len(line)-1, -1, -1):
        r_line.append(line[i])
    return r_line


# 회문 찾는 함수
def my_find():
    for i in range(N):
        # 가로검사
        for j in range(N-M+1):
            tmp = words[i][j:j+M]
            # 회문 검사
            if tmp == my_reverse(tmp):
                return tmp

        # 세로 검사
        for j in range(N-M+1):
            tmp = []  # 부분 문자열을 위한 빈 리스트
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == my_reverse(tmp):
                return tmp
    return []



T = int(input())
for tc in range(1, T+1):
    # N: 2차원 리스트의 크기, M: 회문 길이
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    ans = my_find()
    print("#{} {}".format(tc, ''.join(ans)))