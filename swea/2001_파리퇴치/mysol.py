import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    Max_kill = 0


    # 시작 위치
    for i in range(N-M+1):
        for j in range(N-M+1):

            Sum_kill = 0
            
            
            for k in range(M):
                for l in range(M):
                    Sum_kill += arr[i+k][j+l]


                     
            if Max_kill < Sum_kill:
                Max_kill = Sum_kill
    

            # Max_kill = max(Max_kill,Sum_kill)
        
    
    
    
    print(f'{tc} {Max_kill}')


















    