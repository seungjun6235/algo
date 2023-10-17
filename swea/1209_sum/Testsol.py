import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):

    tc = int(input())

    matrix = []

    # _ => 변수 활용 x 
    for _ in range(100):
        numbers = list(map(int,input().split()))
        matrix.append(numbers)

    max_total = 0

    # 가로줄의 합
    for i in range(len(matrix)):
        total = 0
        for j in range(len(matrix[0])):
            total += matrix[i][j]

        if max_total < total:
            max_total = total

    #세로줄의 합
    for i in range(len(matrix)):
        total = 0
        for j in range(len(matrix[0])):
            total += matrix[j][i]

        if max_total < total:
            max_total = total


    # 대각선의 합
    total = 0
    for i in range(100):
        total += matrix[i][i]

    if max_total < total:
        max_total = total

    # 반대쪽 대각선의합
    total = 0
    for i in range(100):
        total += matrix[i][99-i]

    if max_total < total:
        max_total = total

    print(f'{tc} {max_total}')



