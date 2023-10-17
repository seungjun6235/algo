import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):

    N = int(input()) 

    numbers = list(map(int, input().split()))

    for i in range(N):
        max_Val = max(numbers)
        min_Val = min(numbers)

        min_Idx = numbers.index(min_Val)
        max_Idx = numbers.index(max_Val)

        numbers[max_Idx] -= 1
        numbers[min_Idx] += 1

        if numbers[max_Idx] - numbers[min_Idx] < 2:
            break

    result = max(numbers) - min(numbers)

    print(f'#{tc} {result}')

