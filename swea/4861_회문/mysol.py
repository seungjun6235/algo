import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())

    arr = list(input() for _ in range(N))

    result = ''

    for i in range(N):
        
        
        for j in range(N-M+1):
            
            temp = []

            for k in range(M):
                temp += arr [i][j+k]

            if temp == temp[::-1]:
                result = ''.join(temp)
                


        for l in range(N-M+1):
            temp = []

            for m in range(M):
                temp += arr [l+m][i]

            if temp == temp[::-1]:
                result = ''.join(temp)
                

    print(result)