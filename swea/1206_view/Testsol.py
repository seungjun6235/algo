import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):

    N = int(input()) 
    buildings = list(map(int, input().split()))

    total = 0

    for i in range(N):
        now = buildings[i]
    
        # 건물 0이면 다음 건물로 이동
        if now == 0:
            continue

        
   
        else:
            idx = [-2,-1,1,2]

            Side_building_max = 0

            for j in range(4):

                comparison = buildings[i+idx[j]]

                if Side_building_max < comparison:
                    Side_building_max = comparison

            if now > Side_building_max:
                view_count = now - Side_building_max
                total += view_count
                
                

    print(f'#{tc} {total}')