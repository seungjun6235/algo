import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10

    memo = [0,1,3]

    while N >= len(memo):
        memo.append(memo[len(memo)-1] + 2 * memo[len(memo)-2])

    print(f'#{tc} {memo[N]}')

