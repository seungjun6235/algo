import sys
sys.stdin = open('input.txt')

def search(idx):
    if idx >= N:
        print(result)
        return
    
    for i in range(N):
        # print(idx, i, '=', arr[idx][i])
        result.append(arr[idx][i])
        search(idx+1)
        result.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []

    search(0)
