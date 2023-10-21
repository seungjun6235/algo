import sys
sys.stdin = open('input.txt')


def Myfind():
    for i in range(N):
        for j in range(N-M+1):
            temp = arr [i][j:j+M]

            if temp == temp[::-1]:
                return temp

    
        for k in range(N-M+1):
            temp = []
            for l in range(M):
                temp.append(arr[k+l][i])

            if temp == temp[::-1]:
                return ''.join(temp)

  
T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    print(f'#{tc} {Myfind()}')










    
        
    

        