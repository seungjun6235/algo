import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    temp = []

    while len(arr) > 0:
        max_num = max(arr)
        arr.remove(max_num)
        temp.append(max_num)

        min_num = min(arr)
        arr.remove(min_num)
        temp.append(min_num)

        if len(temp) == 10:
            break
    
    result = ' '.join(list(map(str,temp)))

    print(f'{tc} {result}')