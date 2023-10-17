import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):

    N,M = list(map(int, input().split())) 

    numbers = list(map(int, input().split()))

    blank = []

    for i in range(N-M+1):
        temp_value =0
        for j in range(i,i+M):
            temp_value += numbers[j]

        blank.append(temp_value)

    answer = max(blank) - min(blank)

        


    print(f'#{tc} {answer}')