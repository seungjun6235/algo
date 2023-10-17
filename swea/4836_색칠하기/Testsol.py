import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())

    arr = [[0] * 10 for _ in range(10)]

    purple = 0

    for i in range(N):
        color_data = list(map(int,input().split()))

        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]
        color = color_data[4]

        
        for x in range(left_top_x,right_bottom_x+1):
            for y in range(left_top_y,right_bottom_y+1):
                arr[x][y] += color
                if arr[x][y] == 3:
                    purple += 1

    
    print(f'#{tc} {purple}')

   
