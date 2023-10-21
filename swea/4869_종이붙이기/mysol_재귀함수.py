import sys
sys.stdin = open('input.txt')

T = int(input())

def rec_func(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        return rec_func(N-1) + 2 * rec_func(N-2)
 





for tc in range(1, T+1):
    N = int(input())
       
    print(f'#{tc} {rec_func(N/10)}')