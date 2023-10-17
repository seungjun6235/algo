import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):

    N = int(input()) 

    numbers = list(map(int, input().split()))

    result = 0    

    for i in range(2,N-2):
        arr_max = max(numbers[i-1],numbers[i-2],numbers[i+1],numbers[i+2])

        if numbers[i] > arr_max:
            result += numbers[i] - arr_max

    print(f'#{tc} {result}')