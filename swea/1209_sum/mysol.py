import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):

    tc_num = int(input())

    matrix = [list(map(int, input().split())) for _ in range(100)]
   

    #가로줄의 합
    max_1 = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += matrix [i][j]
        if sum > max_1:
            max_1 = sum

    #세로줄의 합
    max_2 = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += matrix [j][i]
        if sum > max_2:
            max_2 = sum

    #대각선의 합

    max_3 = 0
    for i in range(100):
        sum = 0
        sum += matrix [i][i]
    if sum > max_3:
        max_3 = sum

    # 반대 대각선의 합

    max_4 = 0
    for i in range(100):
        sum = 0
        sum += matrix [i][99-i]
    if sum > max_4:
        max_4 = sum

    print(f'#{tc} {max(max_1,max_2,max_3,max_4)}')