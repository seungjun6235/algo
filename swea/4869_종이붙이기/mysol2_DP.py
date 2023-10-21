import sys
sys.stdin = open('input.txt')

T = int(input())

def DP_func(N):
    memo = [0,1,3]

    for i in range(3,N+1):
        memo.append(memo[i-1]+ 2 * memo[i-2])
    
    return memo[N]






for tc in range(1, T+1):
    N = int(input()) // 10

    print(f'#{tc} {DP_func(N)}')