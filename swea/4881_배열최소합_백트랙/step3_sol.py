import sys
sys.stdin = open('input.txt')

def search(idx):
    global sum, min_sum

    if idx >= N:
        
        if sum < min_sum:
            min_sum = sum
            
        return
    
    #모든 경우의 수 탐색
    for i in range(N):
        if not visited[i]:
            # print(idx, i, '=', arr[idx][i])
            # result.append(arr[idx][i])
            sum += arr[idx][i]
            visited[i] = True
            search(idx+1)
            # result.pop()
            sum -= arr[idx][i]
            visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    visited = [False] * N


    sum = 0
    min_sum = 10000000

    search(0)
