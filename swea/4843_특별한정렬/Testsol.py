import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    temp = []

    while True:
        max_num = 0

        for i in range(len(arr)):
            if max_num < arr[i]:
                max_num = arr[i]
        
        arr.remove(max_num)
        temp.append(max_num)


        min_num = 100000000

        for i in range(len(arr)):
            if min_num > arr[i]:
                min_num = arr[i]
        
        arr.remove(min_num)
        temp.append(min_num)

        if len(temp) == 10:
            break

    result = ' '.join(list(map(str, temp)))

    print(f'#{tc} {result}')
    
    

        

    