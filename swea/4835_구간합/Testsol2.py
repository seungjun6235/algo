import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    Numbers = list(map(int, input().split()))

    min_total = 100000000
    max_total = 0


    for i in range(N-M+1):
        temp_value = 0
        for j in range(M):
            temp_value += Numbers[i+j]

        if temp_value < min_total:
            min_total = temp_value

        if temp_value > max_total:
            max_total = temp_value

    result = max_total - min_total

    print(f'#{tc} {result}')

