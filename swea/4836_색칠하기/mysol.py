import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())

    arr = [[0] * 10 for _ in range(10)]
    purple = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color
                if arr[i][j] == 3:
                    purple += 1

    print(f'#{tc} {purple}')