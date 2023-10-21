import sys
sys.stdin = open('input.txt')

def get_min_sum(row,now_sum):
    global min_sum

    if row == len(arr):
        min_sum = min(min_sum, now_sum)
    elif now_sum > min_sum:
        return
    else:
        for col in range(len(arr)):
            if not visited[col]:
                visited[col] = True
                get_min_sum(row+1,now_sum+arr[row][col])
                visited[col] = False



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N

    min_sum = 10000000

    get_min_sum(0,0)

    print(min_sum)


   