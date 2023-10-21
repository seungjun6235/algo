import sys
sys.stdin = open('input.txt')

def search(idx):
    if idx >= N:
        print(result)
        return
    
    #모든 경우의 수 탐색
    for i in range(N):
        if not visited[i]:
             # print(idx, i, '=', arr[idx][i])
            result.append(arr[idx][i])
            visited[i] = True
            search(idx+1)
            result.pop()
            visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    visited = [False] * N

    search(0)
