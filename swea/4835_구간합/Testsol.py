import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    TC = list(map(int, input().split()))


    max_value = 0
    min_value = 123456

    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += TC[i+j]

        if temp > max_value:
            max_value = temp
        if temp < min_value:
            min_value = temp

    ans = max_value - min_value

    print('#{} {}'.format(tc, ans))